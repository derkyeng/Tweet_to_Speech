import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_text_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT text FROM tweets")

    rows = cur.fetchall()
    text_list = []
    for row in rows:
        text_list.append(row[0])

    return text_list
