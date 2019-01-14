import datetime
from flask import Flask, render_template, request, session# Import the class `Flask` from the `flask` module, written by someone else.
from flask_session import Session
#export FLASK_APP=application.py
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker



app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session (app)

engine = create_engine("postgres://ayjxjjxhgpzlnl:f150cc319da46e38a1fb398ee335d98fa5468668d0d8aa3da415aed475d08f9b@ec2-54-225-227-125.compute-1.amazonaws.com:5432/d9prh5mib7dh2p") #talk to datbase wiTh SQL. Object used to manage connections to database.  
#Sending data to and from database
db = scoped_session(sessionmaker(bind=engine)) # for individual sessions

#note_pad = []

db.execute("CREATE TABLE flights(id SERIAL PRIMARY KEY, origin VARCHAR NOT NULL, destination VARCHAR NOT NULL, duration INTEGER NOT NULL)")

db.execute("INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'London', 415)")
db.execute("INSERT INTO flights (origin, destination, duration) VALUES ('Istanbul', 'Tokyo', 700)")
flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
#for flight in flights
#print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

print(flights)

@app.route("/", methods = ["GET", "POST"]) # A decorator; when the user goes to the route `/`, exceute the function immediately below
def index():
	
	#conditional
	#now = datetime.datetime.now()
	#new_year = now.month == 12 and now.day == 25
	new_year = True
	#return render_template("index.html", new_year=new_year)

	#for looop
	names = ["Alice", "Bob", "Cahlelie"]
	#return render_template("index.html", names=names)

	#return "Hello World"
	headline = "Hello Russ"
	return render_template("index.html", headline=headline, names=names, new_year=new_year)

@app.route("/notes", methods = ["GET", "POST"])
def notes():
	if session.get("note_pad") is None:
			session["note_pad"] = []	

	if request.method=="POST":
		note = 	request.form.get("note")
		print (note)
		session["note_pad"].append(note)
		print (session["note_pad"])
		#note_pad.append(note)
		return render_template("notes.html", note_pad=session["note_pad"]) 
	else: 	
		return render_template("notes.html")

@app.route("/hello", methods = ["POST"])
def hello():
	if request.method=="GET":
		return "please submit form"
	else:	
		name = 	request.form.get("name")
		return render_template("hello.html", name=name)

@app.route("/more")
def more():
	return render_template("about.html")	

@app.route("/bye")
def bye():
	headline = "goodbye"
	return render_template("about.html")	

@app.route("/inherit", methods = ["GET", "POST"])
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


