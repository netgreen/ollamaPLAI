from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()  # מקבל JSON
    return jsonify({"received": data}), 200

if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0', port=8000)
