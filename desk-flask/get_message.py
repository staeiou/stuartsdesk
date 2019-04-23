import slack_login
#import tweepy
import pytz
import os
import datetime
import slackclient

def get_message_text():
    with open("/home/pi/stuartsdesk/status.txt") as f:
        return f.read()

def get_message():
    
    slack_token = slack_login.slack_token
    
    sc = SlackClient(slack_token)
    
    hist = sc.api_call("conversations.history",channel=slack_login.channel)
    
    msg = hist['messages'][0]['text']
    
    timestamp = hist['messages'][0]['ts']
    
    date_formatted = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    
    time_formatted = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')

    return msg, date_formatted, time_formatted

def get_message_twitter():
    #assert True is False
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

