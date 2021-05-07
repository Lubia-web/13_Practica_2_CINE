import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_cinema")

cursor = connection.cursor()
cursor.execute("show tables")
for table in cursor:
    print(table)
connection.close()