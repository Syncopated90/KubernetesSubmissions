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
    print(os.environ['PINGPONG_URL'])
    response = requests.get(os.environ['PINGPONG_URL'])
    ping = response.text
    #ping = 4
    filename = "config/information.txt"
    #os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "r") as message_file:
        message = message_file.read()
    return (f'<div>Env variable: {message}</div>\
            <div>{date_and_hash()}</div><div>Ping / pongs: {ping}</div>\
                ')

#Opens on port 8000
if __name__ == "__main__":
    if os.environ.get('PORT') is not None:
        print("Server started in port " + str(os.environ['PORT']))
        log_output.run(host="0.0.0.0", port=os.environ['PORT'])
    else:
        print("Server started in port 8000")
        log_output.run(host="0.0.0.0", port=8000)
