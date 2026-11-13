import os, random, string
import logging
from flask import Flask
import sys

cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

def random_hash():
    return ''.join(random.choices(string.ascii_letters + string.digits, k = 16))

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = True
process_hash = random_hash()

@app.route("/")
def index():
    return (f'<div>Process hash:{process_hash} </div> <div>New hash: {random_hash()}</div>')

#is run by PORT=1234 python app.py to open on port 1234
if __name__ == '__main__':
    if os.environ.get('PORT') is not None:
        print("Server started in port " + str(os.environ['PORT']))
        app.run(host="0.0.0.0", port=os.environ['PORT'])
    else:
        print("Server started in port 8000")
        app.run(host="0.0.0.0", port=8000)
    