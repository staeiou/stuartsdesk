import slack_login
#import tweepy
import pytz
import os
import datetime
from slackclient import SlackClient

def get_message_text():
    with open("/home/pi/stuartsdesk/status.txt") as f:
        return f.read()

def get_message():

#    print("starting get_message()")
    
    slack_token = slack_login.slack_token
    
    sc = SlackClient(slack_token)

#    print("authenticated with slack")
    
    hist = sc.api_call("conversations.history",channel=slack_login.channel)
    
    msg = hist['messages'][0]['text']
    
    timestamp = float(hist['messages'][0]['ts'])

    gmt = pytz.timezone('GMT')
    pacific = pytz.timezone('US/Pacific')

    gmt_date = gmt.localize(timestamp)

    pacific_date  = gmt_date.astimezone(pacific)
    
    date_formatted = datetime.datetime.fromtimestamp(timestamp).strftime("%a %d %b %Y")
    
    time_formatted = datetime.datetime.fromtimestamp(timestamp).strftime("%I:%M %p")

#    print("returning message")

    return msg, date_formatted, time_formatted

