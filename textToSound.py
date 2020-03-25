import sqlite3
from os.path import dirname, abspath
from reader import create_connection, select_text_tasks
from gtts import gTTS

def main():
    text_to_speech_list = []
    count = 0
    d = dirname(abspath(__file__))
    database = d + r"\twitter2.db"

    conn = create_connection(database)
    with conn:
        text_to_speech_list = select_text_tasks(conn)

    for my_text in text_to_speech_list:
        myobj = gTTS(text=my_text, lang='en', slow=False)
        myobj.save(str(count) + ".mp3")
        count += 1

if __name__ == '__main__':
    main()
