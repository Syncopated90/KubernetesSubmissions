from flask import Flask, request, jsonify
import psycopg2
import os

todo_backend = Flask(__name__)

def connect_to_db():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database= os.environ["DB_NAME"],
        user= os.environ["DB_USER"],
        password= os.environ["DB_PASSWORD"]
    )
    return conn
def store_todo(conn, todo):
    cur = conn.cursor()
    cur.execute("INSERT INTO Todos (todo) VALUES (%s)", (todo,))
    conn.commit()
def get_todos(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Todos")
    conn.commit()
    results = cur.fetchall()
    '''print(results)
    print(type(results))
    print(results[0])
    print(type(results[0]))
    print(results[0][0])
    print(type(results[0][0]))'''
    todos = []
    for (_, todo) in results:
        todos.append(todo)
    return todos

@todo_backend.route('/get-todo-list', methods=['GET'])
def get_lists():
    conn = connect_to_db()
    todos = get_todos(conn)
    conn.close()
    return jsonify(todos)

@todo_backend.route('/post-todo-item', methods=['POST'])
def post_lists():
    conn = connect_to_db()
    todo_added = request.form['text']
    print(todo_added)
    store_todo(conn, todo_added)
    conn.close()
    return jsonify(success=True)

if __name__ == '__main__':
    if os.environ.get('PORT') is not None:
        print("Server started in port " + str(os.environ['PORT']))
        todo_backend.run(host="0.0.0.0", port=os.environ['PORT'])
    else:
        print("Server started in port 8000")
        todo_backend.run(host="0.0.0.0", port=8000)

#TODO write correct sql calls from this part and it should work?