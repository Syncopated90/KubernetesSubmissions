from time import sleep
import os, random, string, datetime
from flask import Flask

log_output = Flask(__name__)
def main():
    logger()

@log_output.route("/")
def index():
    filename = "files/logged.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "r+") as log_file:
        return f'<div>{log_file.read()}</div>'    
    return (f'<div>no log found</div>')

#Opens on port 8001
if __name__ == "__main__":
    if os.environ.get('PORT') is not None:
        print("Server started in port " + str(os.environ['PORT']))
        log_output.run(host="0.0.0.0", port=os.environ['PORT'])
    else:
        print("Server started in port 8000")
        log_output.run(host="0.0.0.0", port=8000)
