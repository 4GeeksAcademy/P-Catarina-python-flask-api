from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    if not todos:
        return '<h2>You have 0 tasks</h2>'
    else:
        return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return get_todos()

@app.route('/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    print("Request to delete task: ", str(index))
    todos.pop(index - 1)
    return get_todos()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)