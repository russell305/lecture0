import datetime
from flask import Flask, render_template # Import the class `Flask` from the `flask` module, written by someone else.
#export FLASK_APP=application.py

app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file

@app.route("/") # A decorator; when the user goes to the route `/`, exceute the function immediately below
def index():
	#conditional
	#now = datetime.datetime.now()
	#new_year = now.month == 12 and now.day == 25
	#return render_template("index.html", new_year=new_year)

	#for looop
	#names = ["Alice", "Bob", "Cahlelie"]
	#return render_template("index.html", names=names)

	#return "Hello World"
	headline = "Hello Russ"
	return render_template("index.html", headline=headline)

@app.route("/more")
def more():
	return render_template("about.html")	

@app.route("/bye")
def bye():
	headline = "goodbye"
	return render_template("about.html")	

@app.route("/inherit")
def inherit():
	return render_template("inherit.html")

@app.route("/inherit1")
def inherit1():
	return render_template("inherit1.html")	


#@app.route("/david")
#def david():
	#return "Hello David"

#@app.route("/<string:name>")
#def hello(name):
	#name=name.capitalize()
	#return f"Hello, {name}!"