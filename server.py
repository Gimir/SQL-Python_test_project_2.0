from flask import Flask, render_template, request
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def list():
	return render_template('list.html')

@app.route('/add')
def add():
	return render_template('add.html')

if __name__ == '__main__':
	app.run(debug=True)
