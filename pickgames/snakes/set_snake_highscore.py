import mysql.connector
from MySQLdb.constants.FIELD_TYPE import VARCHAR

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="game_dev"
)


def save_high_score(score, name):
    curr_score = score
    save_name = str(name)
    query = mydb.cursor()
    query.execute(
        "SELECT score,name FROM high_score where type = 'snake' ORDER BY score DESC, NAME ASC LIMIT 1;")
    fetch = query.fetchall()

    if not fetch and curr_score != 0:
        query = mydb.cursor()
        insert = "INSERT INTO high_score (name, score, categories, type) VALUES (%s, %s, %s, %s)"
        value = (save_name, curr_score, 'N/A', 'snake')
        query.execute(insert, value)
        mydb.commit()
    else:
        high_score = fetch [0] [0]
        if curr_score >= high_score:
            query = mydb.cursor()
            insert = "INSERT INTO high_score (name, score, categories, type) VALUES (%s, %s, %s, %s)"
            value = (save_name, curr_score, 'N/A', 'snake')
            query.execute(insert, value)
            mydb.commit()


def display_HighScore():
    query = mydb.cursor()

    query.execute(
        "SELECT name,score FROM high_score where type = 'snake' ORDER BY  score DESC, NAME ASC LIMIT 1;")

    fetch = query.fetchall()

    if not fetch:
        for score in fetch:
            return score
    else:
        for score in fetch:
            return score
