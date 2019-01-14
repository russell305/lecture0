
#TODO uninstall postgress 11, downlaod 10
#how to create a database table
#create columns
CREATE TABLE flights(id SERIAL PRIMARY KEY, origin VARCHAR NOT NULL, destination VARCHAR NOT NULL, duration INTEGER NOT NULL);

#INSERT
#inserting (or write )a row into database
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'London', 415);
INSERT INTO flights (origin, destination, duration) VALUES ('Istanbul', 'Tokyo', 700);
	 

#SELECT (reading rows in a database)
SELECT * FROM flights;  #asterisk means select all columns from flights table
#whole table shown

SELECT origin, destination FROM flights;
#shows these colmns from rows

SELECT * FROM flights WHERE id = 3; # where restrict the rows with WHERE
SELECT * FROM flights WHERE origin = 'New York';
SELECT * FROM flights WHERE duration > 500;
SELECT * FROM flights WHERE destination = 'Paris' AND duration > 500;
SELECT * FROM flights WHERE destination = 'Paris' OR duration > 500; 

SELECT destination, duration FROM flights;

#functions
SELECT AVG(duration) FROM flights;
SELECT AVG(duration) FROM flights WHERE origin = "New York";
SELECT COUNT(*) FROM flights;
SELECT COUNT(*) FROM flights WHERE origin = "New York";
SELECT MIN(duration) FROM flights
SELECT * FROM flights WHERE duration = "245";
SELECT * FROM flights WHERE origin IN ('New York', 'Lima');
SELECT * FROM flights WHERE origin LIKE '%a%'; # any origin that has an 'a' surrounded by text %=placeholder text



#UPDATE changing data
UPDATE flights SET duration = 430 WHERE origin = "New York" AND destination = "London";

#DELETE
DELETE FROM flights WHERE destination = "Tokyo";

#LIMIT limit the amount of results you get back
SELECT * FROM flights LIMIT 2;  #return 2 rows

#ORDER list by ascending order
SELECT * FROM flights ORDER BY duration ASC;
SELECT * FROM flights ORDER BY duration DESC;

SELECT * FROM flights ORDER BY duration ASC LIMIT 3; # 3 shortest flights

SELECT origin, COUNT(*) FROM flights GROUP BY origin;
#shows all origins and shows count

SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;
#shows all origins that appear more than once and how many of each

#add foreign key to connect 2 tables
CREATE TABLE passengers(
	id SERIAL PRIMARY KEY,
	name VARCHAR NOT NULL,
	flight_id INTEGER REFERENCES flights #refences id or PRIMARY KEY from another table
);

INSERT INTO passengers (name, flight_id) VALUES ('Alice', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Bob', 3);
INSERT INTO passengers (name, flight_id) VALUES ('Charlie', 2);

SELECT * FROM passengers WHERE name = 'Alice'; # get id then call it, not best way
SELECT * FROM flights WHERE id = 1;

#JOIN defaults to INNER = only get the things that match

SELECT origin, destination, name FROM flights INNER JOIN passengers ON flights.id = passengers.flight_id;
#shows columns (origin destination name) that order with all passengers and their origin destination name

SELECT origin, destination, name FROM flights INNER JOIN passengers ON flights.id = passengers.flight_id WHERE name = 'Alice';
#shows columns with Alice row only.

SELECT origin, destination, name FROM flights LEFT JOIN passengers ON flights.id = passengers.flight_id;
#LEFT JOIN means still show all rows on Left table (flights) even if they dont have a match 

SELECT flight_id FROM passengers GROUP BY flight_id HAVING COUNT(*) > 1;
#show flight_id's with more than 1 passenger

SELECT * FROM flights WHERE id IN(SELECT flight_id FROM passengers GROUP BY flight_id HAVING COUNT(*) > 1);
#nested query
#show all flights with multiple passengers  

#SQL Transactions (race conditions), banking atm
BEGIN
#locks datbase untils all SQL commands in between these are executed
	SELECT balance FROM bank WHERE user_id = 1;
  	UPDATE bank SET balance = balance - 100 WHERE user_id = 1;
COMMIT



	


