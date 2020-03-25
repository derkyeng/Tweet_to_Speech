import tweepy
import sqlite3

conn = sqlite3.connect('twitter2.db')
x = conn.cursor()
x.execute("CREATE TABLE IF NOT EXISTS tweets(text VARCHAR, created_at DATETIME, user_id VARCHAR, user_name VARCHAR)")

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()


    def on_status(self, status):
            x.execute("""INSERT INTO tweets (text,created_at,user_id,user_name) VALUES(?,?,?,?)""",
            (status.text, status.created_at, status.user.id, status.user.name))
            conn.commit()
            print(status.text)

    def on_error(self, status_code):
        print(sys.stderr, 'Encountered error with status code:', status_code)
        return True

    def on_timeout(self):
        print(sys.stderr, 'Timeout...')
        return True

def main():
    follow_list = ["19701628", "759251", "15012486", "2149888183"]
    scrape = tweepy.streaming.Stream(auth, CustomStreamListener(api))
    scrape.filter(follow=follow_list)

if __name__ == '__main__':
    main()
