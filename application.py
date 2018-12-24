from flask import Flask, render_template # Import the class `Flask` from the `flask` module, written by someone else.
#export FLASK_APP=application.py

app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file

@app.route("/") # A decorator; when the user goes to the route `/`, exceute the function immediately below
def index():
	#return "Hello World"
	headline = "Hello Russ"
	return render_template("index.html", headline=headline)

#@app.route("/david")
#def david():
	#return "Hello David"

#@app.route("/<string:name>")
#def hello(name):
	#name=name.capitalize()q
	#return f"Hello, {name}!"