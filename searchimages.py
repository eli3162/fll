from flask import *
import logging, os, json, subprocess, pathlib, requests, uuid, logging, sys, textwrap, hashlib
app = Flask(__name__)

@app.route('/')
def check():
    return 'Flask'

if __name__ == '__main__':
    app.run()