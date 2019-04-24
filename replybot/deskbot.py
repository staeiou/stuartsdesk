from slackbot.bot import default_reply
from slackbot.bot import respond_to
from slackbot import settings

@respond_to('')
def my_default_handler(message):
    with open("/home/pi/stuartsdesk/desk-flask/status.txt") as f:
        status = f.read()

    message.reply(status)


