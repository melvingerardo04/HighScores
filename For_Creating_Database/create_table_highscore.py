import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="game_dev"
)

# create database
query = mydb.cursor()
query.execute(
    "CREATE TABLE high_score (id INT (11) NOT NULL PRIMARY KEY AUTO_INCREMENT,"
    "name VARCHAR (255), score INT (11),categories VARCHAR (50),"
    "type VARCHAR (50), date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP )"
)
fetch = query.fetchall()
