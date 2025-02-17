from flask import Flask, request, jsonify
from model import init,init_conversation, chat

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/setRegText', methods=['POST'])
def setRegText():
	regJson = request.get_json();
	regText = regJson['regText'];
	
	f = open("/app/regDic.txt", "w")
	f.write(regText)
	f.close()
	
	init()
	init_conversation()
	
	return jsonify("setRegText success"), 200;
    
@app.route('/askQuestion', methods=['POST'])
def askQuestion():
    	questionJson = request.get_json();
    	question = questionJson['question'];
    	print("askQuestion - " + question)
    	
    	return chat(question), 200
	
if __name__ == '__main__':
	init()
	init_conversation()
	app.run(debug=True, host='0.0.0.0', port=8000);
