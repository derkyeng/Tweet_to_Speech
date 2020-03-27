import sqlite3
import os
from os.path import dirname, abspath
from gtts import gTTS

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


def main():
    text_to_speech_list = []
    count = 0
    d = dirname(abspath(__file__))
    database = d + r"\twitter2.db"

    conn = create_connection(database)
    save_to = dirname(abspath(__file__)) + r"\tweets_mp3"
    with conn:
        text_to_speech_list = select_text_tasks(conn)

    for my_text in text_to_speech_list:
        myobj = gTTS(text=my_text, lang='en', slow=False)
        myobj.save("%s.mp3" % os.path.join(save_to, str(count)))
        count += 1

if __name__ == '__main__':
    main()
