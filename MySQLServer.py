import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Denomdemon12.",
    database="alx_book_store"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
# for i in mycursor:
#     print(i)
