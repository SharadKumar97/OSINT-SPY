import re
import sqlite3

def getEmails(path):
    match_list = []
    regex_match = re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    # connect to database
    db = sqlite3.connect(path)
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master where type='table'")
    tables = cursor.fetchall()
    # finding out email addresses in table
    for table in tables:
        print "[*] Scanning tables....%s" % table
        # now let select everything
        cursor.execute("SELECT * FROM %s" % table[0])
        rows = cursor.fetchall()
        for row in rows:
            for column in row:
                try:
                    matches = regex_match.findall(column)
                except:
                    continue
                for match in matches:
                    if match not in match_list:
                        match_list.append(match)
    cursor.close()
    db.close()
    print "[*] Discovered %d matches :" % len(match_list)
    for match in match_list:
        print "Email's Found ::"+match
# string for contact [a-zA-Z0-9_.+-]+[a-zA-Z0-9-]+[a-zA-Z0-9-.]+
def getContacts(path):
    list=[]
    regex_match = re.compile('([A-Z]\w+(?=[\s\-][A-Z])(?:[\s\-][A-Z]\w+)+)')
    db = sqlite3.connect(path)
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master where type='table'")
    tables=cursor.fetchall()
    for table in tables:
        print "[*] Scanning tables....%s" %table
        # now let select everything
        cursor.execute("SELECT * FROM Contacts")
        rows = cursor.fetchall()
        for row in rows:
            for column in row:
                try:
                    matches = regex_match.findall(column)
                except:
                    continue
                for match in matches:
                    if match not in list:
                        list.append(match)
    cursor.close()
    db.close()
    print "[*] Discovered %d matches :" % len(list)
    for match in list:
        print "Contact found ::" + match

def getChat(path):

    list2 = []
    regex_match = re.compile('[a-zA-Z0-9_.+-]+[a-zA-Z0-9-]+[a-zA-Z0-9-.]+')
    db = sqlite3.connect(path)
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master where type='table'")
    tables = cursor.fetchall()
    for table in tables:
        print "[*] Scanning tables....%s" % table
        # now let select everything
        cursor.execute("SELECT * FROM Chats")
        rows = cursor.fetchall()
        for row in rows:
            for column in row:
                try:
                    matches = regex_match.findall(column)
                except:
                    continue
                for match in matches:
                    if match not in list2:
                        list2.append(match)
    cursor.close()
    db.close()
    print "[*] Discovered %d matches :" % len(list2)
    for match in list2:
        print "Chat found ::" + match
