import mysql.connector

try:
    alxbookstore_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Danny@Oracle_25"
    )
    
    mycursor = alxbookstore_db.cursor()
    
    database_name = 'alx_book_store'

    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

    print(f"Database '{database_name}' created successfully!")
    
    mycursor.close()
    alxbookstore_db.close()
    
except mysql.connector.Error as err:
    err = 'Error! Failed to connect.'
    print(err)