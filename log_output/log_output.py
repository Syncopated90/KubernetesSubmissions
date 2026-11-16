from time import sleep
import os, random, string, datetime
from flask import Flask
import requests

log_output = Flask(__name__)

def random_hash():
    return ''.join(random.choices(string.ascii_letters + string.digits, k = 16))
def date_and_hash():
    return str(datetime.datetime.now()) + ': ' + random_hash()

@log_output.route("/")
def index():
    response = requests.get('http://pingpong-svc:2345/pingpong')
    print(response.text)
    ping = response.text
    return (f'<div>{date_and_hash()}</div><div>Ping / pongs: {ping}</div>')

#Opens on port 8001
if __name__ == "__main__":
    if os.environ.get('PORT') is not None:
        print("Server started in port " + str(os.environ['PORT']))
        log_output.run(host="0.0.0.0", port=os.environ['PORT'])
    else:
        print("Server started in port 8000")
        log_output.run(host="0.0.0.0", port=8000)
