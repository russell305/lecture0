#export FLASK_APP=application.py
#export DATABASE_URL="postgres://ayjxjjxhgpzlnl:f150cc319da46e38a1fb398ee335d98fa5468668d0d8aa3da415aed475d08f9b@ec2-54-225-227-125.compute-1.amazonaws.com:5432/d9prh5mib7dh2p"
#key: 0S6vFxQgJiRIw2CZbc2Yg
#secret: 0kmzCjBS62odOXkfg4EcYnoBND3IM28ANuEFlTlWig
#import datetime
from flask import Flask, render_template, request, session# Import the class `Flask` from the `flask` module, written by someone else.
#from flask_session import Session
import os
#import csv
import requests #for JSON

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker



app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file

#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session (app)

engine = create_engine("postgres://ayjxjjxhgpzlnl:f150cc319da46e38a1fb398ee335d98fa5468668d0d8aa3da415aed475d08f9b@ec2-54-225-227-125.compute-1.amazonaws.com:5432/d9prh5mib7dh2p")
#talk to datbase wiTh SQL. Object used to manage connections to database.  
#Sending data to and from database
db = scoped_session(sessionmaker(bind=engine)) # for individual sessions
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "0S6vFxQgJiRIw2CZbc2Yg", "isbns": "9781632168146"})
#print(res.json())
#note_pad = []

#db.execute("CREATE TABLE flights(id SERIAL PRIMARY KEY, origin VARCHAR NOT NULL, destination VARCHAR NOT NULL, duration INTEGER NOT NULL)")
#db.execute("CREATE TABLE books2(id SERIAL PRIMARY KEY, isbn VARCHAR NOT NULL, title VARCHAR NOT NULL, author VARCHAR NOT NULL, year INTEGER NOT NULL)")


	#db.execute("DELETE FROM books1 WHERE id >'29'")
#for i in range(20):
#db.execute("INSERT INTO flights (origin, destination) VALUES ('New Delhi', 'Miami')")
#db.execute("INSERT INTO flights (origin, destination) VALUES ('Atlanta', 'Bogota', '655')")
db.execute("INSERT INTO flights (origin, destination, duration) VALUES ('NY', 'Tokyo', '424')")
#db.commit()


flights = db.execute("SELECT * FROM flights3").fetchall()
books1 = db.execute("SELECT * FROM books_2").fetchall()
#top3= db.execute("SELECT * FROM books_2 ORDER BY id ASC LIMIT 3").fetchall()
#for flight in flights:
	#print(f"{flight.origin} to {flight.destination} minutes.")

print("flights",flights)
print("books1",books1)
#print("top3", top3)


@app.route("/", methods = ["GET", "POST"]) # A decorator; when the user goes to the route `/`, exceute the function immediately below
def index():
	#conditional
	#now = datetime.datetime.now()
	#new_year = now.month == 12 and now.day == 25
	new_year = True
	#return render_template("index.html", new_year=new_year)

	#for looop
	names = books1
	#return render_template("index.html", names=names)

	#return "Hello World"
	headline = "Hello Russ"
	return render_template("index.html", headline=headline, names=names, new_year=new_year)



@app.route("/books", methods= ["GET", "POST"])
def books():
	print("booksalert")
	name = request.form.get("name")
	print(name)
	author=name
	title=name

		
	if db.execute("SELECT * FROM books_2 WHERE title = :title", {"title": title}).rowcount > 0:	
		#book_choice = db.execute("SELECT * FROM books1 WHERE author = :author", {"author": author}).fetchall()
		book_choice = db.execute("SELECT * FROM books1 WHERE title = :title", {"title": title}).fetchall()
		print("book_object= ",book_choice)
		print("russisbn= ", book_choice[0].isbn)
		result = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "0S6vFxQgJiRIw2CZbc2Yg", "isbns": book_choice[0].isbn})
		#print("result",result.json())

		result_1 = result.json()
		result_2 = result_1.get("books")
		#print("result_2 = ",result_2)
		#print("average_rating = ",result_2[0]["average_rating"])
		#print ("result_1= ",result_1[books.average_rating])
		return render_template("hello.html", name=book_choice)

	elif db.execute("SELECT * FROM books_2 WHERE author = :author", {"author": author}).rowcount > 0:	
		#book_choice = db.execute("SELECT * FROM books1 WHERE author = :author", {"author": author}).fetchall()
		book_choice = db.execute("SELECT * FROM books1 WHERE author = :author", {"author": author}).fetchall()
		print("book_object= ",book_choice)
		print("russisbn= ", book_choice[0].isbn)
		result = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "0S6vFxQgJiRIw2CZbc2Yg", "isbns": book_choice[0].isbn})
		print("result",result.json())

		result_1 = result.json()
		result_2 = result_1.get("books")
		print("result_2 = ",result_2)
		print("average_rating = ",result_2[0]["average_rating"])
		#print ("result_1= ",result_1[books.average_rating])
		return render_template("hello.html", name=book_choice)	
	else:	
		return render_template("hello.html", name="no author")

@app.route("/books/<string:title>", methods= ["GET", "POST"])	
def book_description(title):
	print("hhiihii", title)
	return render_template("inherit1.html")		
	
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
		print(name)
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


