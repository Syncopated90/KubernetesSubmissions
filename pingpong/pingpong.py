import os
from flask import Flask
import psycopg2

pingpong = Flask(__name__)

def connect_to_db():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database= os.environ["DB_NAME"],
        user= os.environ["DB_USER"],
        password= os.environ["DB_PASSWORD"]
    )
    return conn

def store_pings(pings, conn):
    cur = conn.cursor()
    cur.execute("UPDATE ping_nr SET pings = %s WHERE ping_id = 1;", (pings,))
    conn.commit()
    return pings
def get_pings(conn):
    cur = conn.cursor()
    cur.execute("SELECT pings FROM ping_nr")
    return cur.fetchall()

@pingpong.route("/pingpong")
def ping_pong():
    if "DB_HOST" not in os.environ:
        ping = 69
        return (f'pong {ping}')
    conn = connect_to_db()
    ping = get_pings(conn)[0][0]
    ping = store_pings(ping + 1, conn)
    conn.close()
    return (f'pong {ping}')
    

@pingpong.route("/pings")
def ping_number():
    if "DB_HOST" not in os.environ:
        ping = 69
        return (f'pong {ping}')
    conn = connect_to_db()
    ping = get_pings(conn)[0][0]
    conn.close()
    return (f"{ping}")

#is run by PORT=1234 python app.py to open on port 1234
if __name__ == '__main__':
    if os.environ.get('PORT') is not None:
        print("Server started in port " + str(os.environ['PORT']))
        pingpong.run(host="0.0.0.0", port=os.environ['PORT'])
    else:
        print("Server started in port 8000")
        pingpong.run(host="0.0.0.0", port=8000)
    