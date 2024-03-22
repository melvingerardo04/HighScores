import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="game_dev"
)


def saveHighScore(name, current_score, get_highscore, difficulties):
    if get_highscore is not None:
        high_score = get_highscore[0]
    else:
        high_score = current_score
    if current_score >= high_score != 0:
        query = mydb.cursor()
        insert = "INSERT INTO high_score (name, score, categories, type) VALUES (%s, %s, %s, %s)"
        value = (name, current_score, difficulties, 'tetris')
        query.execute(insert, value)
        mydb.commit()
        return "You Beat High score"
    else:
        return "Better luck next time"


def displayEasyHighScore(score):
    if score is not None:
        query = mydb.cursor()
        query.execute(
            "SELECT score,name FROM high_score WHERE categories = 'Easy' AND type= 'tetris'  ORDER BY  score DESC, NAME ASC LIMIT 1;")
        fetch = query.fetchall()
        for score in fetch:
            return score
    else:
        return score


def displayMediumHighScore(score):
    if score is not None:
        query = mydb.cursor()
        query.execute("SELECT score,name FROM high_score WHERE categories = 'medium' AND type= 'tetris' ORDER BY  score DESC, NAME ASC LIMIT 1;")
        fetch = query.fetchall()
        for score in fetch:
            return score
    else:
        return score


def displayHardHighScore(score):
    query = mydb.cursor()
    query.execute("SELECT score,name FROM high_score WHERE categories = 'hard' AND type= 'tetris' ORDER BY  score DESC, NAME ASC LIMIT 1;")
    fetch = query.fetchall()
    for score in fetch:
        return score
