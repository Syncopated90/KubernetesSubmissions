from flask import Flask, request, jsonify
import os

todo_backend = Flask(__name__)

todo_list = ["feed the cats", "do the dishes"]

@todo_backend.route('/get-todo-list', methods=['GET'])
def get_lists():
    return jsonify(todo_list)

@todo_backend.route('/post-todo-item', methods=['POST'])
def post_lists():
    todo_added = request.form['text']
    print(todo_added)
    todo_list.append(todo_added)
    return jsonify(success=True)

if __name__ == '__main__':
    if os.environ.get('PORT') is not None:
        print("Server started in port " + str(os.environ['PORT']))
        todo_backend.run(host="0.0.0.0", port=os.environ['PORT'])
    else:
        print("Server started in port 8000")
        todo_backend.run(host="0.0.0.0", port=8000)