import win32com.client
import datetime
import psycopg2
import time


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


def convert_from_ol(s):
    return str(datetime.datetime.strptime((s[:-8] + s[17:19]), "%Y-%m-%d %H:%M:%S"))


def compare_datetimes(s_db, s_ol):
    s_db = datetime.datetime.strptime(s_db, "%Y-%m-%d %H:%M:%S")
    s_ol = datetime.datetime.strptime(s_ol, "%Y-%m-%d %H:%M:%S")
    if s_db < s_ol:
        return True
    else:
        return False


def stringify(attribute):
    return "'" + attribute + "'"


class Conversation:
    def __init__(self):
        self.messageID = None
        self.sender = None
        self.body = None
        self.sent_on = None


class Outlook:
    def __init__(self):
        self.outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace(
            "MAPI"
        )
        self.accounts = win32com.client.Dispatch("Outlook.Application").Session.Accounts
        self.start()

    def start(self):
        while True:
            for account in self.accounts:
                self.inbox = self.outlook.GetDefaultFolder(6)
                self.messages = self.inbox.Items
                self.conversations = []
                print(len(self.inbox.Items))
                for msg in self.messages:
                    if msg.Class != 43:
                        continue
                    else:
                        self.convo = Conversation()
                        self.convo.messageID = msg.ConversationID
                        if len(msg.SenderEmailAddress) > 64:
                            if msg.Class == 43 and msg.SenderEmailType == "EX":
                                self.convo.sender = (
                                    msg.Sender.GetExchangeUser().PrimarySmtpAddress
                                )
                        else:
                            self.convo.sender = msg.SenderEmailAddress
                        self.convo.sent_on = convert_from_ol(str(msg.SentOn))
                        self.convo.body = msg.HTMLBody
                        self.conversations.append(self.convo)
                        print("Added")
                connection = db_connect()
                cursor = connection.cursor()

                email_map = {"someone@domain.com.com": "someones_table"}

                for i in self.conversations:
                    print(email_map[(account.displayName).lower()])
                    cursor.execute(
                        "SELECT EXISTS(SELECT 1 FROM %s WHERE email = %%s)"
                        % (email_map[(account.displayName).lower()]),
                        [i.sender],
                    )
                    result = cursor.fetchone()[0]
                    if result == False:
                        print(i.sender, "not in db", result)
                        print("Checking if", i.sender, "in contacts")
                        cursor.execute(
                            "SELECT EXISTS(SELECT 1 FROM contacts WHERE email_1 = %s OR email_2 = %s OR email_3 = %s)",
                            (i.sender, i.sender, i.sender),
                        )
                        result = cursor.fetchone()[0]
                        if result == True and i.sender != "":
                            cursor.execute(
                                "INSERT INTO %s VALUES (%%s, %%s, %%s)"
                                % (email_map[(account.displayName).lower()]),
                                [i.sender, i.sent_on, i.body],
                            )
                            connection.commit()
                        else:
                            print(
                                "Cannot add",
                                i.sender,
                                "to email_history since they do not appear in your contacts",
                            )
                    else:
                        print(i.sender, "already in db ", result)
                        cursor.execute(
                            "SELECT datetime from %s WHERE email = %%s"
                            % (email_map[(account.displayName).lower()]),
                            [i.sender],
                        )
                        result = cursor.fetchone()[0]
                        update = compare_datetimes(result, i.sent_on)
                        if update == True:
                            print(
                                "Updated",
                                i.sender,
                                "because",
                                result,
                                " is older than",
                                i.sent_on,
                            )
                            cursor.execute(
                                "UPDATE %s SET body = %%s, datetime = %%s WHERE email = %%s"
                                % (email_map[(account.displayName).lower()]),
                                [i.body, i.sent_on, i.sender],
                            )
                            connection.commit()
                    time.sleep(0.1)
                cursor.close()
                connection.close()
                print("Now starting on", account.DisplayName)
                time.sleep(1)
            time.sleep(30)


Outlook()
