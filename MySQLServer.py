import mysql.connector

try:
    alxbookstore_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Danny@Oracle_25"
    )
    
    mycursor = alxbookstore_db.cursor()
    
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS alx_book_store")

    print(f"Database 'alx_book_store' created successfully!")
    
    mycursor.close()
    alxbookstore_db.close()
    
except mysql.connector.Error as err:
    err = 'Error! Failed to connect.'
    print(err)