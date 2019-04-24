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
    
    hist_from_self = []

    for msg in hist['messages']:
        if msg['user'] == slack_login.sender_id:
            hist_from_self.append(msg)

    msg = hist_from_self[0]['text']
    
    timestamp = datetime.datetime.fromtimestamp(float(hist['messages'][0]['ts']))

    gmt = pytz.timezone('GMT')
    pacific = pytz.timezone('US/Pacific')

    gmt_date = gmt.localize(timestamp)

    pacific_date  = gmt_date.astimezone(pacific)
    
    date_formatted = pacific_date.strftime("%a %d %b %Y")
    
    time_formatted = pacific_date.strftime("%I:%M %p")

    with open("/home/pi/stuartsdesk/desk-flask/status.txt", "w+") as f:
        f.write(msg + "\n")
        f.write("This was last updated at " + time_formatted + ", " + date_formatted)

#    print("returning message")

    return msg, date_formatted, time_formatted

