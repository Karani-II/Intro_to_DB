import mysql.connector 
mydb = mysql.connector.connect(
    host = "local host",
    user = "root",
    password = "Karani8411@",
)
try:
    mycursor = mydb.cursor()
    mycursor.Execute("""CREATE DATABASE IF NOT EXISTS alx_book_store""")
    print("Database 'alx_book_store' created successfully!")
except mysql.connctor.Error:
    print("Could not connect to the database")
mycursor.close()

