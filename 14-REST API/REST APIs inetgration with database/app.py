from flask import Flask,request, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/')
def greet():
	return jsonify({'message':'This is a project to udertsand REST APIs with python'})


@app.route('/display_users')
def display_users():
	connection = sqlite3.connect('data.db')
	cursor = connection.cursor()
	query = "SELECT * FROM users"
	result = cursor.execute(query)
	items = []
	for row in result:
		items.append({'username': row[1], 'password': row[2]})
	connection.close()
	return jsonify({'items': items})


@app.route('/adduser', methods = ['POST'])
def add_user():
	user_dict = request.get_json()
	id_ = user_dict['ID']
	username = user_dict['USERNAME']
	password = user_dict['PASSWORD']
	connection = sqlite3.connect('data.db')
	cursor = connection.cursor()
	query = "INSERT INTO users VALUES(?, ?, ?)"
	cursor.execute(query, (id_, username, password))
	connection.commit()
	connection.close()
	return jsonify({'message':'user added'})


app.run(port=5000)


        


