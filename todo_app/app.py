import os, random, string, datetime
import logging
from flask import Flask, render_template, url_for
import sys
from pathlib import Path
from shutil import copyfileobj
from urllib.request import urlopen

cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

def download_image(url, destination):
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with urlopen(url, timeout=30) as response, destination.open("wb") as image_file:
        copyfileobj(response, image_file)

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = True
download_image("https://picsum.photos/1200", os.path.join(app.static_folder, "image.jpg"))
image_time = datetime.datetime.now()

@app.route("/")
def index():
    global image_time
    print((image_time - datetime.timedelta(minutes=10)))
    if (image_time + datetime.timedelta(minutes=10)) < datetime.datetime.now():
        image_time = datetime.datetime.now()
        download_image("https://picsum.photos/1200", os.path.join(app.static_folder, "image.jpg"))
    return render_template("index.html", image=url_for("static", filename="image.jpg"))
    
#is run by PORT=1234 python app.py to open on port 1234
if __name__ == '__main__':
    if os.environ.get('PORT') is not None:
        print("Server started in port " + str(os.environ['PORT']))
        app.run(host="0.0.0.0", port=os.environ['PORT'])
    else:
        print("Server started in port 8000")
        app.run(host="0.0.0.0", port=8000)
    