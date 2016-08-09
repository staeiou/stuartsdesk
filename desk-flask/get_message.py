import twitter_login
import tweepy
import pytz

def get_message():

    auth = tweepy.OAuthHandler(twitter_login.consumer_key, twitter_login.consumer_secret)
    auth.set_access_token(twitter_login.token_key, twitter_login.token_secret)

    api = tweepy.API(auth)

    msgs = api.direct_messages()
    msg = msgs[0]

    gmt = pytz.timezone('GMT')
    pacific = pytz.timezone('US/Pacific')

    gmt_date = gmt.localize(msg.created_at)

    pacific_date  = gmt_date.astimezone(pacific)

    date_formatted = pacific_date.strftime("%a %d %b %Y")
    time_formatted = pacific_date.strftime("%I:%M %p")

    return msg.text, date_formatted, time_formatted

