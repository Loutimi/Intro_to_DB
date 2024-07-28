import mysql.connector

# FOR EXCEPTION HANDLING
try:
        
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Denomdemon12.",
        database = 'alx_book_store',
    )
    if mydb.is_connected():
        # TO CHECK IF THE DATABASE CONNECTS
        print("Database 'alx_book_store' created successfully!")
    
    else:
        # USING EXECUTE FUNCTION TO CREATE DATABASE IF IT DOESN'T EXIST
        cursor = mydb.cursor()
        cursor.execute('CREATE DATABASE IF NOT EXISTS alx_book_store')

except mysql.connector.Error as er:
    print("Something went wrong: {}".format(er))
