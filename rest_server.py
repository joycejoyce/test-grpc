# rest_server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify(result=data['a'] + data['b'])

if __name__ == '__main__':
    app.run(port=5000)
