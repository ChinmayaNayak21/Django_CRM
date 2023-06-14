import mysql.connector


database = mysql.connector.connect(
    host="localhost", 
    user='root', 
    password="Chinu@9821", 
    )
cursor = database.cursor()
cursor.execute("CREATE DATABASE elderco")
print("done")
