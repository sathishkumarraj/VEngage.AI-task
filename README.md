# Vengage.Ai_Assessment

Goal: Implement backend code for the
following problem statements

Problem 1:
Write a method that reads phone book records from a CSV or JSON file.
Each record consists of the following parameters Name, email, Phone 1, Phone 2.

Problem 2:
Implement a SQL-like parser for phone book records in Problem 1 to implement CRUD
operaNons and print SQL like output on console.:
2.1
SELECT * FROM phone_records; This statement reads the first 10 records and displays them
on the console.

2.2
SELECT * FROM phone_records WHERE name=’doe’; this statement filters the records and
displays the record(s) where ‘Doe’ is found.
2.3
INSERT INTO phone_records(name, email,phone 1, phone 2)
VALUES(‘Test’,’test@test.xtyz’,’1234456’,’1233233’)
This statement should create a new entry in the dataset and the same should be obtained
when execuNng secNon 2.2 (i.e. the previous example)

2.4
DELETE FROM phone_records WHERE name=’John’
This statement should delete the record from the dataset.
