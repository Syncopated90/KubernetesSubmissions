from time import sleep
import os, random, string, datetime
from flask import Flask

log_output = Flask(__name__)
def main():
    logger()
def random_hash():
    return ''.join(random.choices(string.ascii_letters + string.digits, k = 16))

def logger():
    while(True):
        sleep(5)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k = 16))
        print(str(datetime.datetime.now()) + ': ' + random_string)

@log_output.route("/")
def index():
    return (f'<div>New hash: {random_hash()}</div>')

#Opens on port 8001
if __name__ == "__main__":
    if os.environ.get('PORT') is not None:
        print("Server started in port " + str(os.environ['PORT']))
        log_output.run(host="0.0.0.0", port=os.environ['PORT'])
    else:
        print("Server started in port 8000")
        log_output.run(host="0.0.0.0", port=8000)
