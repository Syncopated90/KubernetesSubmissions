import os
import logging
from flask import Flask
import sys

cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None


app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = True

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#is run by PORT=1234 python app.py to open on port 8000
if __name__ == '__main__':
    if os.environ.get('PORT') is not None:
        print("Server started in port " + str(os.environ['PORT']))
        app.run(host="0.0.0.0", port=os.environ['PORT'])
    else:
        print("Server started in port 8000")
        app.run(host="0.0.0.0", port=8000)
    