import psycopg2


def apostrophe_check(attribute):
    if attribute is None:
        return attribute
    if "'" in attribute:
        new_attribute = attribute.replace("'", "''")
        return stringify(new_attribute)
    elif attribute != "":
        return stringify(attribute)
    else:
        return attribute


def build_insert_query(query_list):
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute("SELECT MAX(c_id) FROM contacts;")
    max_id = str((cursor.fetchone()[0] + 1))
    cursor.close()
    connection.close()
    statement = "INSERT INTO contacts ("
    feild_map = {}
    for i in range(len(query_list)):
        if query_list[i] != "":
            feild_map[i] = False
        else:
            feild_map[i] = True
    feild_map = list(feild_map.values())
    feild_map.insert(0, False)
    db_list = [
        "c_id",
        "first_name",
        "last_name",
        "company",
        "job_title",
        "email_1",
        "email_2",
        "email_3",
        "phone_1",
        "phone_2",
        "phone_3",
        "street_line_1",
        "street_line_2",
        "city",
        "c_state",
        "zip",
        "notes",
        "category",
    ]
    for i in range(len(feild_map)):
        if feild_map[i] == False:
            statement = statement + db_list[i] + ", "
    statement = statement[:-2] + ") " + "VALUES ("
    query_list.insert(0, max_id)
    for i in range(len(query_list)):
        if feild_map[i] == False:
            statement = statement + query_list[i] + ", "
    return statement[:-2] + ");"


def build_select_query(attribute_list):
    statement = "SELECT * FROM contacts WHERE "
    feild_map = {}
    for i in range(len(attribute_list)):
        if attribute_list[i] != "":
            feild_map[i] = False
        else:
            feild_map[i] = True
    feild_map = list(feild_map.values())
    table_list = [
        "first_name",
        "last_name",
        "company",
        "phone_1",
        "email_1",
        "category",
        "notes",
    ]
    for i in range(len(attribute_list)):
        attribute_list[i] = apostrophe_check(attribute_list[i])
    for i in range(len(feild_map)):
        if feild_map[i] == False:
            statement = statement + table_list[i] + " = " + attribute_list[i] + " AND "
    return statement[:-5] + ";"


def db_connect():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="xyz",
            host="127.0.0.1",
            port="5432",
            database="postgres",
        )
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    return connection


def delete_category(selection):
    try:
        connection = db_connect()
        cursor = connection.cursor()
        cursor.execute("""DELETE FROM categories WHERE category = %s""", (selection,))
        connection.commit()
        cursor.close()
        connection.close()
        return "update"
    except:
        return "query"


def delete_from_id(c_id):
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM contacts WHERE c_id = %s""", (c_id,))
    connection.commit()
    cursor.execute("""SELECT EXISTS(SELECT * FROM contacts WHERE c_id = %s)""", (c_id,))
    result = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return result


def duplicate_query(fname, lname, company, phone_1, phone_2, phone_3, email_1, email_2):
    if fname != "":
        if lname != "":
            if company != "":  # All 3 present
                query = (
                    "SELECT EXISTS(SELECT * FROM contacts WHERE first_name = "
                    + fname
                    + " AND last_name = "
                    + lname
                    + " AND company = "
                    + company
                    + ");"
                )
            elif (
                phone_1 != ""
            ):  # Check for first and last name with phone numbers or emails
                query = (
                    "SELECT EXISTS(SELECT * FROM contacts WHERE first_name = "
                    + fname
                    + " AND last_name = "
                    + lname
                    + " AND phone_1 = "
                    + phone_1
                    + ");"
                )
            elif phone_2 != "":
                query = (
                    "SELECT EXISTS(SELECT * FROM contacts WHERE first_name = "
                    + fname
                    + " AND last_name = "
                    + lname
                    + " AND phone_2 = "
                    + phone_2
                    + ");"
                )
            elif phone_3 != "":
                query = (
                    "SELECT EXISTS(SELECT * FROM contacts WHERE first_name = "
                    + fname
                    + " AND last_name = "
                    + lname
                    + " AND phone_3 = "
                    + phone_3
                    + ");"
                )
            elif email_1 != "":
                query = (
                    "SELECT EXISTS(SELECT * FROM contacts WHERE first_name = "
                    + fname
                    + " AND last_name = "
                    + lname
                    + " AND email_1 = "
                    + email_1
                    + ");"
                )
            elif email_2 != "":
                query = (
                    "SELECT EXISTS(SELECT * FROM contacts WHERE first_name = "
                    + fname
                    + " AND last_name = "
                    + lname
                    + " AND email_2 = "
                    + email_2
                    + ");"
                )
            else:
                query = (
                    "SELECT EXISTS(SELECT * FROM contacts WHERE first_name = "
                    + fname
                    + " AND last_name = "
                    + lname
                    + ");"
                )

        elif company != "":  # first name and company
            query = (
                "SELECT EXISTS(SELECT * FROM contacts WHERE first_name = "
                + fname
                + " AND company = "
                + company
                + ");"
            )
        elif phone_1 != "":  # Check for first only with phone numbers or emails
            query = (
                "SELECT EXISTS(SELECT * FROM contacts WHERE first_name = "
                + fname
                + " AND phone_1 = "
                + phone_1
                + ");"
            )
        elif phone_2 != "":
            query = (
                "SELECT EXISTS(SELECT * FROM contacts WHERE first_name = "
                + fname
                + " AND phone_2 = "
                + phone_2
                + ");"
            )
        elif phone_3 != "":
            query = (
                "SELECT EXISTS(SELECT * FROM contacts WHERE first_name = "
                + fname
                + " AND phone_3 = "
                + phone_3
                + ");"
            )
        elif email_1 != "":
            query = (
                "SELECT EXISTS(SELECT * FROM contacts WHERE first_name = "
                + fname
                + " AND email_1 = "
                + email_1
                + ");"
            )
        elif email_2 != "":
            query = (
                "SELECT EXISTS(SELECT * FROM contacts WHERE first_name = "
                + fname
                + " AND email_2 = "
                + email_2
                + ");"
            )
        else:
            query = None
            print("Error cannot query database by first name only")

    elif lname != "":  # Last name but no first name
        if company != "":  # last name and company
            query = (
                "SELECT EXISTS(SELECT * FROM contacts WHERE last_name = "
                + lname
                + " AND company = "
                + company
                + ");"
            )
        elif phone_1 != "":  # Check for last only with phone numbers or emails
            query = (
                "SELECT EXISTS(SELECT * FROM contacts WHERE last_name = "
                + lname
                + " AND phone_1 = "
                + phone_1
                + ");"
            )
        elif phone_2 != "":
            query = (
                "SELECT EXISTS(SELECT * FROM contacts WHERE last_name = "
                + lname
                + " AND phone_2 = "
                + phone_2
                + ");"
            )
        elif phone_3 != "":
            query = (
                "SELECT EXISTS(SELECT * FROM contacts WHERE last_name = "
                + lname
                + " AND phone_3 = "
                + phone_3
                + ");"
            )
        elif email_1 != "":
            query = (
                "SELECT EXISTS(SELECT * FROM contacts WHERE last_name = "
                + lname
                + " AND email_1 = "
                + email_1
                + ");"
            )
        elif email_2 != "":
            query = (
                "SELECT EXISTS(SELECT * FROM contacts WHERE last_name = "
                + lname
                + " AND email_2 = "
                + email_2
                + ");"
            )
        else:
            query = None
            print("Error cannot query database by last name only")

    elif company != "":  # company only
        if phone_1 != "":
            query = (
                "SELECT EXISTS(SELECT * FROM contacts WHERE company = "
                + company
                + " AND phone_1 = "
                + phone_1
                + ");"
            )
        elif phone_2 != "":
            query = (
                "SELECT EXISTS(SELECT * FROM contacts WHERE company = "
                + company
                + " AND phone_1 = "
                + phone_2
                + ");"
            )
        elif phone_3 != "":
            query = (
                "SELECT EXISTS(SELECT * FROM contacts WHERE company = "
                + company
                + " AND phone_3 = "
                + phone_3
                + ");"
            )
        elif email_1 != "":
            query = (
                "SELECT EXISTS(SELECT * FROM contacts WHERE company = "
                + company
                + " AND email_1 = "
                + email_1
                + ");"
            )
        elif email_2 != "":
            query = (
                "SELECT EXISTS(SELECT * FROM contacts WHERE company = "
                + company
                + " AND email_2 = "
                + email_2
                + ");"
            )
        else:
            query = None
            print("Error cannot search database by company only")
    else:
        return None

    if query is not None:
        connection = db_connect()
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return result
    else:
        return None


def exists_query(query_list):
    for i in range(len(query_list)):
        if i < 3:
            query_list[i] = apostrophe_check(query_list[i])
        else:
            if query_list[i] != "":
                query_list[i] = stringify(query_list[i])
    fname = query_list[0]
    lname = query_list[1]
    company = query_list[2]
    phone_1 = query_list[4]
    phone_2 = query_list[5]
    phone_3 = query_list[6]
    email_1 = query_list[7]
    email_2 = query_list[8]
    duplicate = duplicate_query(
        fname, lname, company, phone_1, phone_2, phone_3, email_1, email_2
    )

    if duplicate == None or duplicate == True:
        return "duplicate"
    else:
        return False


def get_all_categories(c_id=None):
    connection = db_connect()
    cursor = connection.cursor()
    if c_id == None:
        cursor.execute("""SELECT * FROM categories""")
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        results = [i[0] for i in results]
        return results
    else:
        c_id = str(c_id)
        cursor.execute("""SELECT category FROM contacts WHERE c_id = %s""", (c_id,))
        result = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return result


def insert_contact(query_list):
    query = build_insert_query(query_list)
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    try:
        cursor.execute("""UPDATE contacts SET phone_1 =REPLACE(phone_1, '-', '')""")
        connection.commit()
        cursor.execute("""UPDATE contacts SET phone_2 =REPLACE(phone_2, '-', '')""")
        connection.commit()
        cursor.execute("""UPDATE contacts SET phone_3 =REPLACE(phone_3, '-', '')""")
        connection.commit()
        cursor.execute(
            """UPDATE contacts SET street_line_1 =REPLACE(street_line_1, '.', '')"""
        )
        connection.commit()
        cursor.execute(
            """UPDATE contacts SET first_name = '' WHERE first_name IS NULL"""
        )
        connection.commit()
        cursor.execute("""UPDATE contacts SET last_name = '' WHERE last_name IS NULL""")
        connection.commit()
        cursor.execute("""UPDATE contacts SET company = '' WHERE company IS NULL""")
        connection.commit()
        cursor.execute("""UPDATE contacts SET job_title = '' WHERE job_title IS NULL""")
        connection.commit()
        cursor.execute("""UPDATE contacts SET phone_1 = '' WHERE phone_1 IS NULL""")
        connection.commit()
        cursor.execute("""UPDATE contacts SET phone_2 = '' WHERE phone_2 IS NULL""")
        connection.commit()
        cursor.execute("""UPDATE contacts SET phone_3 = '' WHERE phone_3 IS NULL""")
        connection.commit()
        cursor.execute("""UPDATE contacts SET email_1 = '' WHERE email_1 IS NULL""")
        connection.commit()
        cursor.execute("""UPDATE contacts SET email_2 = '' WHERE email_2 IS NULL""")
        connection.commit()
        cursor.execute("""UPDATE contacts SET email_3 = '' WHERE email_3 IS NULL""")
        connection.commit()
        cursor.execute(
            """UPDATE contacts SET street_line_1 = '' WHERE street_line_1 IS NULL"""
        )
        connection.commit()
        cursor.execute(
            """UPDATE contacts SET street_line_2 = '' WHERE street_line_2 IS NULL"""
        )
        connection.commit()
        cursor.execute("""UPDATE contacts SET city = '' WHERE city IS NULL""")
        connection.commit()
        cursor.execute("""UPDATE contacts SET c_state = '' WHERE c_state IS NULL""")
        connection.commit()
        cursor.execute("""UPDATE contacts SET zip = '' WHERE zip IS NULL""")
        connection.commit()
        cursor.execute("""UPDATE contacts SET notes = '' WHERE notes IS NULL""")
        connection.commit()
        cursor.execute("""UPDATE contacts SET keywords = '' WHERE keywords IS NULL""")
        connection.commit()
        cursor.execute("""UPDATE contacts SET category = '' WHERE category IS NULL""")
        connection.commit()
        cursor.close()
        connection.close()
        return "add"
    except:
        cursor.close()
        connection.close()
        return "add"


def make_names(results):
    count = 0
    for i in results:
        i = list(i)
        if isinstance(i[0], float):
            i.pop(0)
        first = i[0]
        last = i[1]
        i.insert(0, first + " " + last)
        i.pop(1)
        i.pop(1)
        results[count] = i
        count += 1
        for i in results:
            for j in i:
                if j == " ":
                    j = ""
    return results


def new_main_category(category):
    try:
        connection = db_connect()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO categories (category) VALUES (%s)""", (category,))
        connection.commit()
        cursor.close()
        connection.close()
        return "update"
    except:
        return "query"


def query_all_contacts():
    connection = db_connect()
    cursor = connection.cursor()
    select_query = """SELECT first_name, last_name, company, phone_1, email_1, category FROM contacts"""
    cursor.execute(select_query)
    connection.commit()
    contacts = list(cursor.fetchall())
    contacts = make_names(contacts)
    cursor.close()
    connection.close()
    return sorted(contacts)


def query_email(email):
    try:
        connection = db_connect()
        cursor = connection.cursor()
        cursor.execute("SELECT body FROM email_justin WHERE email = %s", (email,))
        body = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return body
    except:
        return "<p> No email history found for this client </p>"


def query_last_known(c_id):
    connection = db_connect()
    cursor = connection.cursor()
    query = "SELECT fields FROM last_known WHERE c_id = " + stringify(str(c_id)) + ";"
    cursor.execute(query)
    connection.commit()
    try:
        result = cursor.fetchone()[0]
    except:
        result = None
    if result is not None:
        cursor.close()
        connection.close()
        return result
    else:
        cursor.close()
        connection.close()
        return str([False, False, False, False, False])


def query_one_contact(attributes=None, c_id=None):
    if c_id == None:
        connection = db_connect()
        cursor = connection.cursor()
        query = build_select_query(attributes)
        cursor.execute(query)
        connection.commit()
        contact = cursor.fetchone()
        cursor.close()
        connection.close()
        return contact
    else:
        connection = db_connect()
        cursor = connection.cursor()
        cursor.execute("""SELECT category FROM contacts WHERE c_id = %s""", (c_id,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result is not None and result[0] != "":
            return result[0]
        else:
            return None


def stringify(attribute):
    return "'" + attribute + "'"


def update_category(c_id, selection, delete=None):
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute("""SELECT category FROM contacts WHERE c_id = %s""", (c_id,))
    result = cursor.fetchone()
    if result is not None:
        if result[0] == "":
            cursor.execute(
                """UPDATE contacts SET category = %s WHERE c_id = %s""",
                (
                    selection,
                    c_id,
                ),
            )
            connection.commit()
        else:
            if delete == None:
                selection = result[0] + ";" + selection
                cursor.execute(
                    """UPDATE contacts SET category = %s WHERE c_id = %s""",
                    (
                        selection,
                        c_id,
                    ),
                )
                connection.commit()
            else:
                selection = result[0].replace(selection, "")
                if selection[len(selection) - 1] == ";":
                    selection = selection[:-1]
                if selection[0] == ";":
                    selection = selection[1:]
                cursor.execute(
                    """UPDATE contacts SET category = %s WHERE c_id = %s""",
                    (
                        selection,
                        c_id,
                    ),
                )
                connection.commit()
    else:
        cursor.execute(
            """UPDATE contacts SET category = %s WHERE c_id = %s""",
            (
                selection,
                c_id,
            ),
        )
        connection.commit()
    cursor.execute("""SELECT category FROM contacts WHERE c_id = %s""", (c_id,))
    result = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return result


def update_contact(query_list, c_id):
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute(("SELECT * FROM contacts WHERE c_id = " + str(c_id) + ";"))
    connection.commit()
    comparison_list = cursor.fetchone()
    query = update_query_builder(comparison_list, query_list)
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
    return "update"


def update_last_known(contact_info, c_id):
    connection = db_connect()
    cursor = connection.cursor()
    query = (
        "SELECT EXISTS (SELECT * FROM last_known WHERE c_id = "
        + stringify(str(c_id))
        + ");"
    )
    cursor.execute(query)
    connection.commit()
    result = cursor.fetchone()[0]
    if result == False:
        query = (
            "INSERT INTO last_known VALUES ("
            + stringify(str(c_id))
            + ","
            + stringify(contact_info)
            + ");"
        )
        cursor.execute(query)
        connection.commit()
    else:
        query = (
            "UPDATE last_known SET fields = "
            + stringify(str(contact_info))
            + " WHERE c_id = "
            + stringify(str(c_id))
            + ";"
        )
        cursor.execute(query)
        connection.commit()
    cursor.close()
    connection.close()
    return True


def update_query_builder(comparison, updated):
    statement = "UPDATE contacts SET "
    comparison = list(comparison)
    c_id = comparison[0]
    comparison.pop(0)
    feild_map = {}
    for i in range(len(updated)):
        if updated[i] == comparison[i]:
            feild_map[i] = False
        else:
            feild_map[i] = True
    feild_map = list(feild_map.values())
    db_list = [
        "first_name",
        "last_name",
        "company",
        "job_title",
        "email_1",
        "email_2",
        "phone_1",
        "phone_2",
        "phone_3",
        "street_line_1",
        "street_line_2",
        "city",
        "c_state",
        "zip",
        "notes",
        "category",
    ]
    for i in range(len(updated)):
        updated[i] = apostrophe_check(updated[i])
        if feild_map[i] == True and updated[i] == "":
            updated[i] = "''"
            statement = statement + db_list[i] + " = " + updated[i] + ", "
        elif feild_map[i] == True and updated[i] != "":
            statement = statement + db_list[i] + " = " + updated[i] + ", "
    return statement[:-2] + " WHERE c_id = " + stringify(str(c_id)) + ";"
