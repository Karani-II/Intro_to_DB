import mysql.connector 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Karani8411@",
)
try:
    mycursor = mydb.cursor()
    mycursor.execute("""CREATE DATABASE IF NOT EXISTS alx_book_store""")
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error:
    print("Could not connect to the database")
mycursor.close()

