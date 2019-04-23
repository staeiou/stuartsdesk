from app import app
from get_message import get_message
from send_message import send_message
from flask import Flask, Response, request, redirect
@app.route('/')
@app.route('/index')

def index():

    msg_text, msg_date, msg_time = get_message()    
    #msg_text = get_message()

    html = """<html><head><meta http-equiv="refresh" content="15" />"""
    html += """<style>
    
    div.container {width:460px; height: 300px;}
    div.footer {
    font-size: 24px;
    position: absolute;
    bottom: 5px;
    left: 5px;
    width: 470px;
    height: 30px;
    border: 0px
    }
    div.msg {
    font-size: 55px;
    }
    input { font-size:24px }
    </style>"""
    html += """</head><body><div class="container">"""
    # html += """<iframe align="right" src="http://forecast.io/embed/#lat=37.8699&lon=-122.2705&name=Berkeley" width="200" height="200"></iframe>"""
    html += """<div class="msg">"""
    html += msg_text

    html += """<br/><br/><div class="footer">Sent: """
    html += msg_time
    html += ", "
    html += msg_date
#    html += """<form action="/update" method="post"><input type="submit" name="s" value="Press to ask Stuart for an update"></form></div>"""
    html += """</div></body></html>"""


    return html

import pprint
#@app.route('/update', methods=['GET', 'POST'])
def update():
    #str = pprint.pformat(request.environ, depth=5)
    #return Response(str,mimetype="text/text")
    send_message()

    html = """<html><head><meta http-equiv="refresh" content="3;URL='http://localhost:5000'" /></head>"""
    html += """<body><p style="font-size:50px">Just sent Stuart a message asking for an update</p></body></html>"""

    return html
