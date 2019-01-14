import.os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("database_url")) #talk to datbase wiTh SQL. Object used to manage connections to database.  
#Sending data to and from database
db = scoped_session(sessionmaker(bind=engine)) # for individual sessions

def main():
	flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()  # execute this SQL command and return all of the results
	for flight in flights
		print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.") # for every flight, print out the flight info

if __name__ == "__main__":
	main()