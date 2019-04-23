#!/usr/bin/python3

from flask import Flask, abort, jsonify, render_template, redirect
from werkzeug.exceptions import HTTPException
from app import app
import time


@app.errorhandler(Exception)
def handle_error(e):
    print(e)
    time.sleep(3)
    return redirect("http://localhost:5005/")


app.run(debug=True, host='127.0.0.1', port=5005)
