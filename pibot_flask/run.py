#!flask/bin/python

"""
author: Andriy Rudyk
        Tim Sizemore

date: 21.10.2013

Runs the server.
"""

from app import app
from config import DEBUG

app.run(debug = DEBUG)
