import csv
import psycopg2


class Contact:
    def __init__(self):
        self.id = ""
        self.first_name = ""
        self.last_name = ""
        self.company = ""
        self.job_title = ""
        self.email_1 = ""
        self.email_2 = ""
        self.email_3 = ""
        self.phone_1 = ""
        self.phone_2 = ""
        self.phone_3 = ""
        self.phone_1 = ""
        self.phone_2 = ""
        self.phone_3 = ""
        self.street_line_1 = ""
        self.street_line_2 = ""
        self.city = ""
        self.state = ""
        self.zip_code = ""
        self.notes = ""
        self.placeholder = ""
        self.category = ""


def db_connect():
    try:
        connection = psycopg2.connect(
            user="Postgres",
            password="xyz",
            host="127.0.0.1",
            port="5432",
            database="postgres",
        )
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    return connection


def create_contacts(conn, c):
    cursor = conn.cursor()
    for i in c:
        cursor.execute(
            """INSERT INTO contacts VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (
                (
                    i.id,
                    i.first_name,
                    i.last_name,
                    i.company,
                    i.job_title,
                    i.email_1,
                    i.email_2,
                    i.email_3,
                    i.phone_1,
                    i.phone_2,
                    i.phone_3,
                    i.street_line_1,
                    i.street_line_2,
                    i.city,
                    i.state,
                    i.zip_code,
                    i.notes,
                    i.placeholder,
                    i.category,
                )
            ),
        )
        conn.commit()
    cursor.close()
    conn.close()


def fixphones(p):
    if p != "" and (len(p) > 10):
        c = p
        c = c.replace("+1 ", "")
        c = c.replace("(", "")
        c = c.replace(")", "")
        c = c.replace("#", "")
        while "-" in c:
            c = c.replace("-", "")
        while " " in c:
            c = c.replace(" ", "")
        while "/" in c:
            c = c.replace("/", "")
        c = c.replace(".", "")
        if "ext" in c:
            c = c.replace("ext", "x")
        if "Ext" in c:
            c = c.replace("Ext", "x")
        return c
    else:
        return p


def fill_empty(contact, attr):
    c = contact
    if attr == "phone":
        if c.phone_1 == "":
            if c.phone_2 != "":
                c.phone_1 = c.phone_2
                if c.phone_3 != "":
                    c.phone_2 = c.phone_3
            elif c.phone_3 != "":
                c.phone_1 = c.phone_3
        return c
    else:
        if attr == "email":
            if c.email_1 == "":
                if c.email_2 != "":
                    c.email_1 = c.email_2
                    if c.email_3 != "":
                        c.email_2 = c.email_3
                elif c.email_3 != "":
                    c.email_1 = c.email_3
        return c


def fixemails(contact):
    c = contact
    if c.email_1 in c.email_2:
        c.email_2 = ""
    if c.email_2 in c.email_3:
        c.email_3 = ""
    if c.email_1 in c.email_3:
        c.email_3 = ""
    return c


if __name__ == "__main__":
    with open("export.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        contacts = []
        broken = []
        good = []
        count = 0
        for row in reader:
            c = Contact()
            c.id = count
            c.first_name = row[1]
            c.last_name = row[3]
            c.company = row[5]
            c.category = row[54]
            c.job_title = row[7]
            c.email_1 = row[57]
            c.email_2 = row[59]
            c.email_3 = row[60]
            c.phone_1 = row[31]
            c.phone_2 = row[40]
            c.phone_3 = row[42]
            c.street_line_1 = row[8]
            c.street_line_2 = row[9]
            c.city = row[11]
            c.state = row[12]
            c.zip_code = row[13]
            c.notes = row[77]
            contacts.append(c)
            count += 1

        contacts.pop(0)
        for i in contacts:
            i.phone_1 = fixphones(i.phone_1)
            i.phone_2 = fixphones(i.phone_2)
            i.phone_3 = fixphones(i.phone_3)
            i = fill_empty(i, "phone")
            i = fixemails(i)
            i = fill_empty(i, "email")
    conn = db_connect()
    create_contacts(conn, contacts)
