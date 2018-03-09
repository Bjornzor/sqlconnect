import pymysql.cursors
import sys

#Edit this with your SQLdb settings and account with full privilege
connection = pymysql.connect(
host='localhost',
user='bjorn',
password='VrGTMamZoUpFcnGP',
db='novawebshop',
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)

chosenOption = sys.argv[1]




def usage():
    print("""
        Example:
        1 = sqlquery.py 1 <name> <password>
        2 = sqlquery.py 2 <table>
        """)

def insert(username,password):
    try:
        with connection.cursor() as cursor:
            query = "INSERT INTO `account` (`username`,`password`) VALUES (%s,%s)"
            cursor.execute(query,(username,password))
            connection.commit()
    finally:
        connection.close()

def read(table):
    try:
        with connection.cursor() as cursor:
            query = 'SELECT * FROM `{}`'.format(table)
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                print(row)
            #if result == 0:
            #    dbShow()

    finally:
        connection.close()


options = {'1','2','-h'}

if chosenOption not in options:
    usage()


if chosenOption == '1':
    try:
        unameArg = sys.argv[2]
        passwArg = sys.argv[3]
        insert(unameArg, passwArg)
        print("Account added: {} {}".format(unameArg,passwArg))
    except IndexError:
        usage()

if chosenOption == '2':
    try:
        tableArg = sys.argv[2]
        read(tableArg)
    except IndexError:
        usage()

if chosenOption == '-h':
    usage()
