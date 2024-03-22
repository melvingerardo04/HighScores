import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE Game_Dev")
