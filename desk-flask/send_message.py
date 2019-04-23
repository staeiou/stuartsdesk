#import tweepy
#import twitter_login

def send_message():
    return False

def send_message_twitter():

    auth = tweepy.OAuthHandler(twitter_login.consumer_key, twitter_login.consumer_secret)
    auth.set_access_token(twitter_login.token_key, twitter_login.token_secret)

    api = tweepy.API(auth)

    return api.send_direct_message(screen_name="staeiou", text="Someone at your desk wants an update!")
