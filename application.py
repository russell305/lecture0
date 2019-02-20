#export FLASK_APP=application.py
#export DATABASE_URL="postgres://ayjxjjxhgpzlnl:f150cc319da46e38a1fb398ee335d98fa5468668d0d8aa3da415aed475d08f9b@ec2-54-225-227-125.compute-1.amazonaws.com:5432/d9prh5mib7dh2p"
#key: 0S6vFxQgJiRIw2CZbc2Yg
#secret: 0kmzCjBS62odOXkfg4EcYnoBND3IM28ANuEFlTlWig
#import datetime
from flask import Flask, render_template, request, session, jsonify# Import the class `Flask` from the `flask` module, written by someone else.
from flask_session import Session
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from pprint import pprint
#import csv
import json #for Python to Javascript
import requests #for JSON
from flights import Flight
from mechanic import Mechanic
app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file

GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session (app)

engine = create_engine("postgres://ayjxjjxhgpzlnl:f150cc319da46e38a1fb398ee335d98fa5468668d0d8aa3da415aed475d08f9b@ec2-54-225-227-125.compute-1.amazonaws.com:5432/d9prh5mib7dh2p")
#talk to datbase wiTh SQL. Object used to manage connections to database.
#Sending data to and from database
db = scoped_session(sessionmaker(bind=engine)) # for individual sessions

#russ_api = result = requests.get("http://127.0.0.1:5000/api/flights/7")
#print("russ_api", russ_api)
flight_list=[]
mechanic_list=[]

f1 = Flight(origin="New York", destination="Paris", duration=540)
flight_list.append(f1)
f2 = Flight(origin="la", destination="tokyo", duration=640)
flight_list.append(f2)
f3 = Flight(origin="delaware", destination="italy", duration=6440)
flight_list.append(f3)

#mechanic = Mechanic("russ", "johnson", "12344", "russm305@fmail.com")
#mechanic_list.append(mechanic)

#print("flight", flight_list[2].destination)
#res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "0S6vFxQgJiRIw2CZbc2Yg", "isbns": "9781632168146"})
#print(res.json())
#result_1 = res.json()
#print ("r1",result_1.get("books"))

#note_pad = []

#db.execute("CREATE TABLE flights(id SERIAL PRIMARY KEY, origin VARCHAR NOT NULL, destination VARCHAR NOT NULL, duration INTEGER NOT NULL)")
#db.execute("CREATE TABLE books20(id SERIAL PRIMARY KEY, isbn VARCHAR NOT NULL, title VARCHAR NOT NULL, author VARCHAR NOT NULL, year INTEGER NOT NULL)")

	#db.execute("DELETE FROM books1 WHERE id >'29'")
#for i in range(20):
#db.execute("INSERT INTO flights (origin, destination, duration)  VALUES ('New Delhi', 'Miamibitch', '333')")
#db.execute("INSERT INTO flights (origin, destination, duration)  VALUES ('Atlanta', 'Bogota', '655')")
#db.execute("INSERT INTO flights (origin, destination, duration) VALUES ('NY', 'Tokyo', '424')")
#db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)", {"name": name, "flight_id": flight_id})
name="Rusty2"
phone="786-872-7526"
address= "665 ne 83 terrace"
latitude=25.9757
longitude=-80.3655
email="russm305@gmail.com"
oil_change=5
battery=6
pads_front=8
pads_back=8
starting_problem=8
check_engine=8
tune_up=8
starter=8
alternator=8
spark_plugs=8
valve_cover=8
air_filter=8
mobile_mechanic=True
air_conditioning=False
auto_body=True
tire_rotation=None#check these  threewhen form goes to databas
fix_flat=None
car_wash=None



flights = db.execute("SELECT * FROM flights").fetchall()

#books1 = db.execute("SELECT * FROM books_2").fetchall()
#top3= db.execute("SELECT * FROM books_2 ORDER BY id ASC LIMIT 3").fetchall()
#for flight in flights:
	#print(f"{flight.origin} to {flight.destination} minutes.")

	#wont need this, set up database to take data from form and geocode and update datbase
#for i in flights:


print("flights",flights)
print("flights",flights[0])
print("flights",flights[1].origin)
#print("books1",books1)
#print("top3", top3)
flight_origin =[]
len(flight_origin)




#db.execute("CREATE TABLE mechanic(id SERIAL PRIMARY KEY, name VARCHAR NOT NULL, phone VARCHAR NOT NULL, address VARCHAR NOT NULL, latitude FLOAT NOT NULL, longitude FLOAT NOT NULL, email VARCHAR, oil_change SMALLINT NOT NULL, battery SMALLINT NOT NULL, pads_front SMALLINT NOT NULL, pads_back SMALLINT NOT NULL, starting_problem SMALLINT NOT NULL, check_engine SMALLINT NOT NULL, tune_up SMALLINT NOT NULL, starter SMALLINT NOT NULL, alternator SMALLINT NOT NULL, spark_plugs SMALLINT NOT NULL, valve_cover SMALLINT NOT NULL, air_filter SMALLINT NOT NULL, mobile_mechanic BOOLEAN NOT NULL, air_conditioning BOOLEAN NOT NULL, auto_body BOOLEAN NOT NULL, tire_rotation BOOLEAN NOT NULL, fix_flat BOOLEAN NOT NULL, car_wash BOOLEAN NOT NULL)")
#db.commit()

@app.route("/", methods = ["GET"]) # A decorator; when the user goes to the route `/`, exceute the function immediately below
def index():

	names = "books1"#made string easyiness
	new_year = True
	headline = "Hello Russ"
	return render_template("index.html", headline=headline, names=names, new_year=new_year)

@app.route("/inherit1", methods = ["POST"])
def inherit1():
	name = request.form.get("name")
	phone = request.form.get("phone")
	street = request.form.get("street")
	city = request.form.get("city")
	state = request.form.get("state")
	zip_code = request.form.get("zip_code")
	email = request.form.get("email")
	description = request.form.get("description")
	oil_change = request.form.get("oil_change")
	battery = request.form.get("battery")
	pads_front = request.form.get("pads_front")
	pads_back = request.form.get("pads_back")
	starting_problem= request.form.get("starting_problem")
	check_engine = request.form.get("check_engine")
	tune_up = request.form.get("tune_up")
	starter = request.form.get("starter")
	alternator = request.form.get("alternator")
	spark_plugs = request.form.get("spark_plugs")
	valve_cover = request.form.get("valve_cover")
	air_filter = request.form.get("air_filter")
	mobile_mechanic = request.form.get("mobile_mechanic")
	air_conditioning = request.form.get("air_conditioning")
	auto_body = request.form.get("auto_body")
	tire_rotation = request.form.get("tire_rotation")
	fix_flat = request.form.get("fix_flat")
	car_wash = request.form.get("car_wash")
	address = street+", "+city+", "+state+", "+zip_code
	print(address)

	if mobile_mechanic=="on":
		mobile_mechanic=True
	else:
		mobile_mechanic=False

	if air_conditioning=="on":
		air_conditioning=True
	else:
		air_conditioning=False

	if auto_body=="on":
		auto_body=True
	else:
		auto_body=False

	if fix_flat=="on":
		fix_flat=True
	else:
		fix_flat=False

	if tire_rotation=="on":
		tire_rotation=True
	else:
		tire_rotation=False

	if car_wash=="on":
		car_wash=True
	else:
		car_wash=False


	params = {
		'address': address,
		'key': 'AIzaSyD9fytSdXXr6kVZdXLddFJyF9HT4JTt-qM',
	}
	res = requests.get(GOOGLE_MAPS_API_URL, params=params)
	response = res.json()
	#print("jsonresonse",response)
	latlng=response['results'][0]['geometry']['location']
	latitude = latlng['lat']
	longitude = latlng['lng']
	print("lat", latlng['lat'])
	print("lng", latlng['lng'])


	#before sign up check
	#if session.get("id_table") not None:
		#user_id=session["id_table"][0]
		#print("user already exists", user_id)

	db.execute("INSERT INTO mechanic (name, phone, address, latitude, longitude, email, oil_change, battery, pads_front, pads_back, starting_problem, check_engine, tune_up, starter, alternator, spark_plugs, valve_cover, air_filter, mobile_mechanic, air_conditioning, auto_body, tire_rotation, fix_flat, car_wash) VALUES (:name, :phone, :address, :latitude, :longitude, :email, :oil_change, :battery, :pads_front, :pads_back, :starting_problem, :check_engine, :tune_up, :starter, :alternator, :spark_plugs, :valve_cover, :air_filter, :mobile_mechanic, :air_conditioning, :auto_body, :tire_rotation, :fix_flat, :car_wash)", {"name":name, "phone":phone, "address":address, "latitude":latitude, "longitude":longitude, "email":email, "oil_change":oil_change, "battery":battery, "pads_front":pads_front, "pads_back":pads_back, "starting_problem":starting_problem, "check_engine":check_engine, "tune_up":tune_up, "starter":starter, "alternator":alternator, "spark_plugs":spark_plugs, "valve_cover":valve_cover, "air_filter":air_filter, "mobile_mechanic":mobile_mechanic, "air_conditioning":air_conditioning, "auto_body":auto_body, "tire_rotation":tire_rotation, "fix_flat":fix_flat, "car_wash":car_wash})
	db.commit()
	#after 1st sign up get id_table with ps-id
	#if session.get("id_table") is None:
        #session["id_table"] = []
        #session["id_table"].append(1)



	mechanicsD = db.execute("SELECT * FROM mechanic").fetchall()
	print("mechanicsD",mechanicsD)
	for i in mechanicsD:
		print("mechanicsD",i)

	mechanic = Mechanic( name, email, phone, address, description)
	mechanic_list.append(mechanic)
	for i in mechanic_list:
		try:
		  mech_num
		except NameError:
		  mech_num=0
		  print ("well, it WASN'T defined after all!")
		else:
		  print ("sure, it was defined.")
		  #mech_num = mech_num + 1

		mechanic_name={'mechanic_name': i.name}
		mechanic_email={'mechanic_email': i.email}
		mechanic_phone={'mechanic_phone': i.phone}
		mechanic_address={'mechanic_address': i.address}
		mechanic_description={'mechanic_address': i.description}
		pprint(vars(mechanic_list[mech_num]))


	for i in flights:

		#origin = {'origin': i.origin}
		origin = {
			"origin": i.origin,
			"destination": i.destination,
			"duration": i.duration,
			}
		print ("origin",origin)
		flight_origin.append(origin)

	print("flight_origin", flight_origin)
	print("flight_origin", flight_origin[1])
	List_length = len(flight_origin)
	print("List_length",List_length)



#//I can use mechanic_name instaed of mechanic_id
	mechanic_id = 0
	mechanic_idj={'mechanic_idj': mechanic_id}

	print("mechanic_name", mechanic_name["mechanic_name"])
	return render_template("inherit1.html",mechanicsD=mechanicsD, flight_origin=flight_origin,  mechanic_name=mechanic_name, mechanic_phone=mechanic_phone, mechanic_list=mechanic_list, mechanic_address=mechanic_address,  mechanic_id=mechanic_id, mechanic_idj=mechanic_idj )

@app.route("/mechanic/<string:full_name>")
def mechanic(full_name):
	"Individual Mechanic Data"
	print(full_name)
	for i in mechanic_list:
		if i.full_name == full_name:
			mechanic = i
	return render_template("mechanic.html", mechanic=mechanic)

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
		print("result_2 = ",result_2)
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




#@app.route("/david")
#def david():
	#return "Hello David"

#@app.route("/<string:name>")
#def hello(name):
	#name=name.capitalize()
	#return f"Hello, {name}!"
