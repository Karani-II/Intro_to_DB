import mysql.connector 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Karani8411@",
    database = "alx_book_store"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
Print("Tables in alx_book_store")
for (table) in mycursor:
print(table)
