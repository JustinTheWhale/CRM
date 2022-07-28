from db import db_connect

def search_query(s):
    query = "SELECT first_name, last_name, company, phone_1, email_1, category FROM contacts WHERE LOWER (first_name) LIKE LOWER (%(s)s) OR LOWER (last_name) LIKE %(s)s OR LOWER (company) LIKE LOWER (%(s)s) OR LOWER (job_title) LIKE %(s)s OR LOWER (email_1) LIKE LOWER (%(s)s) OR LOWER (email_2) LIKE %(s)s OR LOWER (phone_1) LIKE LOWER (%(s)s) OR LOWER (phone_2) LIKE %(s)s OR LOWER (phone_3) LIKE LOWER (%(s)s) OR LOWER (street_line_1) LIKE %(s)s OR LOWER (street_line_2) LIKE LOWER (%(s)s) OR LOWER (city) LIKE %(s)s OR LOWER (c_state) LIKE LOWER (%(s)s) OR LOWER (zip) LIKE %(s)s OR LOWER (keywords) LIKE LOWER (%(s)s) OR LOWER (category) LIKE LOWER(%(s)s) ORDER BY first_name, last_name LIMIT 20" % { 's': s }
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def search_space_query(s):
    query = "SELECT set_limit(0.1);"
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.execute("""(SELECT similarity(first_name || ' ' || last_name, %s) AS similarity, first_name, last_name, company, phone_1, email_1, category FROM contacts WHERE  LOWER(first_name || ' ' || last_name) %% LOWER(%s)) UNION ALL (SELECT similarity(company, %s) AS similarity, first_name, last_name, company, phone_1, email_1, category FROM contacts WHERE  LOWER(company) %% LOWER(%s)) UNION ALL (SELECT similarity(category, %s) AS similarity, first_name, last_name, company, phone_1, email_1, category FROM contacts WHERE LOWER(category) %% LOWER(%s)) ORDER BY similarity DESC LIMIT 25""" % (s,s,s,s,s,s,) )
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def set_Qcompleter():
        connection = db_connect()
        statement = """SELECT * FROM contacts;"""
        cursor = connection.cursor()
        cursor.execute(statement)
        contacts = cursor.fetchall()
        qcompleter = []
        seen = {}
        for i in contacts:
            for j in range(len(i)):
                if j != 0 and j != 16:
                    if i[j] != '' and i[j] != None:
                        if i[j] not in seen:
                            qcompleter.append(str(i[j]))
                            seen[i[j]] = None
        return qcompleter


def dup_search(fields):
    query = "SELECT set_limit(1.0);"
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    c_ids = {}
    s = fields[0][:-1] + " " + fields[1][1:]
    if s != '':
        cursor.execute("""SELECT similarity(first_name || ' ' || last_name, %s) AS similarity, c_id FROM contacts WHERE  LOWER(first_name || ' ' || last_name) %% LOWER(%s) ORDER BY similarity DESC LIMIT 15""" % (s,s,) )
        results = cursor.fetchall()
        for i in results:
            if i[1] in c_ids:
                c_ids[i[1]] += 1
            else:
                c_ids[i[1]] = 1
    
    s = fields[2]
    if s != '':
        cursor.execute("""SELECT similarity(company, %s) AS similarity, c_id FROM contacts WHERE  LOWER(company) %% LOWER(%s) ORDER BY similarity DESC LIMIT 15""" % (s,s,) )
        results = cursor.fetchall()
        for i in results:
                if i[1] in c_ids:
                    c_ids[i[1]] += 1
                else:
                    c_ids[i[1]] = 1

    s = fields[3]
    if s != '':
        cursor.execute("""SELECT similarity(phone_1, %s) AS similarity, c_id FROM contacts WHERE  LOWER(phone_1) %% LOWER(%s) ORDER BY similarity DESC LIMIT 15""" % (s,s,) )
        results = cursor.fetchall()
        for i in results:
                if i[1] in c_ids:
                    c_ids[i[1]] += 1
                else:
                    c_ids[i[1]] = 1
    
    s = fields[4]
    if s != '':
        cursor.execute("""SELECT similarity(email_1, %s) AS similarity, c_id FROM contacts WHERE  LOWER(email_1) %% LOWER(%s) ORDER BY similarity DESC LIMIT 15""" % (s,s,) )
        results = cursor.fetchall()
        for i in results:
                if i[1] in c_ids:
                    c_ids[i[1]] += 1
                else:
                    c_ids[i[1]] = 1
    cursor.close()
    connection.close()
    return  c_ids