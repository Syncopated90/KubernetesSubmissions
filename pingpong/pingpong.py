import os
from flask import Flask

pingpong = Flask(__name__)
ping = 0

@pingpong.route("/pingpong")
def ping_pong():
    global ping
    ping += 1
    return (f'<div>pong {ping}</div>')

#is run by PORT=1234 python app.py to open on port 1234
if __name__ == '__main__':
    if os.environ.get('PORT') is not None:
        print("Server started in port " + str(os.environ['PORT']))
        pingpong.run(host="0.0.0.0", port=os.environ['PORT'])
    else:
        print("Server started in port 8000")
        pingpong.run(host="0.0.0.0", port=8000)
    