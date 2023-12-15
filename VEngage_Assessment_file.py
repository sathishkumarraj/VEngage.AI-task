#!/usr/bin/env python
# coding: utf-8

# # Problem 1: 
# Write a method that reads phone book records from a CSV or JSON file 
# Each record consists of the following parameters Name, email, Phone 1, Phone 2.

# In[1]:


import csv


# In[3]:


def read_csv(file_path):
    """
    Reads a CSV file and returns the data as a list of dictionaries.
    
    Parameters:
        file_path (str): The path to the CSV file.
        
    Returns:
        list: A list of dictionaries where each dictionary represents a row in the CSV file.
    """
    data = []

    try:
        with open(file_path, 'r') as file:
            # Create a CSV reader object
            csv_reader = csv.DictReader(file)
            
            # Iterate through each row in the CSV file
            for row in csv_reader:
                # Append each row as a dictionary to the data list
                data.append(dict(row))
                
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error reading CSV file: {e}")

    return data

# Call the function:
file_path = "C:\\Users\\HP\\Desktop\\files of sessions\\Vengage_Assessment\\phone_book_records.csv" # Path of CSV file from my pc
csv_data = read_csv(file_path)

# Display the read data
for row in csv_data:
    print(row)


# In[4]:


# Importing pandas for creating DataFrame
import pandas as pd 


# In[5]:


Phone_Records=pd.DataFrame(csv_data)
Phone_Records


# # Problem 2:
# Implement a SQL-like parser for phone book records in Problem 1 to implement CRUD
# operations and print SQL like output on console.

# # CONNECTION WITH MYSQL DATABASE & PYTHON

# In[11]:


# pip install pymysql


# In[6]:


# Importing numpy and pymysql 
import numpy as np
import pymysql


# In[7]:


# Connection between python and MySQL
myconnection = pymysql.connect(host = "127.0.0.1",user = "root",passwd = "Aradhana@2509")


# In[8]:


cur = myconnection.cursor()


# In[15]:


#Creating New Database
cur.execute("create database PhoneBook_Records");


# In[9]:


cur.execute("use PhoneBook_Records");


# In[10]:


# Makes connection with our Database Named : "PhoneBook_Records"
myconnection = pymysql.connect(host = "127.0.0.1",user = "root",passwd = "Aradhana@2509",database = "PhoneBook_Records");


# In[11]:


cur = myconnection.cursor()


# # CREATE TABLE

# In[45]:


# Create table named Phone_Records
cur.execute("create table Phone_Records(Name varchar(50),Email varchar(50),Phone1 varchar(20),Phone2 varchar(20))")


# # INSERT THE DATAFRAME(TABLE) FROM PYTHON TO DATABASE

# In[46]:


# Inserts values into table named Phone_Records
sql="insert into Phone_Records(Name,Email,Phone1,Phone2)values(%s,%s,%s,%s)";


# In[47]:


# Used loop condition for inserting rows from CSV file
for i in range(0,len(Phone_Records)):
    cur.execute(sql,tuple(Phone_Records.iloc[i]))
    myconnection.commit()
# Inserted successfully


# # 2.1
# SELECT * FROM phone_records; This statement reads the first 10 records and displays them
# on the console.

# In[47]:


# Displays only first 10 records from table
cur.execute("SELECT * FROM Phone_Records ORDER BY Name LIMIT 10"); 


# In[48]:


# Used for loops for fetching first 10 rows
rows=cur.fetchall()
for row in rows:
    print(row)


# # READ THE TABLE FROM DATABASE

# # Tuple View

# In[48]:


# Used loop condition for Reading the values got inserted(view in tuple)  - Table name :Phone_Records
for i in range(0,len(Phone_Records)):
    print(tuple(Phone_Records.iloc[i]))


# # View with index location & data type

# In[49]:


# Used loop condition for Reading the values got inserted(index and datatype displayed) - Table name :Phone_Records
for i in range(0,len(Phone_Records)):
    print(Phone_Records.iloc[i])


# # 2.2
# SELECT * FROM phone_records WHERE name=’Test’; this statement filters the records and
# displays the record(s) where ‘Test’ is found.

# In[60]:


cur.execute('Select * FROM phone_records WHERE name= "Test"');


# In[61]:


# Fetch the result
row = cur.fetchone()

# Check if the row exists
if row:
    print("Selected Row:", row)
else:
    print("Row not found.")
# Got the output which satisfies the condition and the row we have inserted in 2.3 problem 


# # UPDATE COMMAND

# In[22]:


cur.execute("UPDATE Phone_Records SET Phone1 = '8761122208'WHERE Name = 'John'");


# In[23]:


myconnection.commit()


# In[28]:


# After Update Check whether values got updated frome field Name : John
cur.execute("Select*from Phone_Records");


# In[29]:


# Used for loops for fetching all rows
rows=cur.fetchall()
for row in rows:
    print(row)
# In the output ,  the values are updated in the given condition


# # INSERT COMMAND

# # 2.3
# INSERT INTO phone_records(name, email,phone 1, phone 2)
# VALUES(‘Test’,’test@test.xtyz’,’1234456’,’1233233’)
# This statement should create a new entry in the dataset and the same should be obtained
# when execuNng secNon 2.2 (i.e. the previous example)

# In[56]:


cur.execute("INSERT INTO Phone_Records(Name,Email,Phone1,Phone2) VALUES ('Test','test@test.xtyz','1234456','1233233');");


# In[57]:


myconnection.commit()


# In[58]:


cur.execute("Select*from Phone_Records");


# In[59]:


# Used for loops for fetching all rows

rows=cur.fetchall()
for row in rows:
    print(row)
    
# In the output , the values are Inserted in the given condition


# # DELETE COMMAND

# # 2.4
# DELETE FROM phone_records WHERE name=’John’
# This statement should delete the record from the dataset.

# In[63]:


cur.execute("Delete from Phone_Records WHERE Name ='John'");


# In[64]:


myconnection.commit()


# In[65]:


# After Delete Check whether values got Deleted
cur.execute("Select*from Phone_Records");


# In[66]:


# Used for loops for fetching all rows
rows=cur.fetchall()
for row in rows:
    print(row)
# In the output , the values are Deleted in the given condition


# # ANOTHER METHOD
# Using Classes & Methods ==>> Table creation and Performed CRUD opertion using def Function

# In[46]:


class Phonebook_Database:
    def __init__(self):
        self.tables = {}

    def create_table(self,Phonebook_Records, columns): # Function for Create 
        self.tables[Phonebook_Records] = {'columns': columns, 'data': []}

    def insert_into(self,Phonebook_Records, values): # Function for Inserting
        table = self.tables[Phonebook_Records]
        if len(values) != len(table['columns']):
            raise ValueError('Number of values does not match the number of columns.')

        row = dict(zip(table['columns'], values))
        table['data'].append(row)

    def select_all_from(self,Phonebook_Records): # Function for reading
        table = self.tables.get(Phonebook_Records)
        if table:
            return table['data']
        else:
            raise ValueError(f"Table '{Phonebook_Records}' does not exist.")

    def update(self,Phonebook_Records, set_values, where_condition): # function for Updating
        table = self.tables.get(Phonebook_Records)
        if table:
            for row in table['data']:
                if all(row[column] == value for column, value in where_condition.items()):
                    row.update(set_values)
        else:
            raise ValueError(f"Table '{Phonebook_Records}' does not exist.")

    def delete_from(self,Phonebook_Records, where_condition): # Function for Deleting
        table = self.tables.get(Phonebook_Records)
        if table:
            table['data'] = [row for row in table['data'] if not all(row[column] == value for column, value in where_condition.items())]
        else:
            raise ValueError(f"Table '{Phonebook_Records}' does not exist.")

    def print_table(self,Phonebook_Records): # Function for displaying all records in table
        table = self.tables.get(Phonebook_Records)
        if table:
            print(f"Table: {Phonebook_Records}")
            print("Columns:", table['columns'])
            print("Data:")
            for row in table['data']:
                print(row)
        else:
            raise ValueError(f"Table '{Phonebook_Records}' does not exist.")


# Creating and inserting in table:
db = Phonebook_Database()
db.create_table('Phonebook_Records', ['Name', 'Email', 'Phone1','Phone2'])
db.insert_into('Phonebook_Records', ['Karthika priyadharshini','karthikapriya1@gmail.com',8148642615,6380278156])
db.insert_into('Phonebook_Records', ['Aradhana','Aradhana25@gmail.com',9367906789,7809875345])
db.insert_into('Phonebook_Records', ['Parimala','parimala12@gmail.com',8237569990,8754907536])
db.insert_into('Phonebook_Records', ['Pranesh','pranesh1895@gmail.com',9944489573,9786543568])
db.insert_into('Phonebook_Records', ['Baladhandapani','bala1948@gmail.com',8764904578,9764285557])
db.insert_into('Phonebook_Records', ['Yuvaraj','raj211984@gmail.com',8629076622,9788207652])
db.insert_into('Phonebook_Records', ['Shobana','abc22@gmail.com',9747734667,7866695679])
db.insert_into('Phonebook_Records', ['John','john12@gmail.com',8546890343,9123457899])
db.insert_into('Phonebook_Records', ['Roby','roby34@gmail.com',9765785767,9567833988])
db.insert_into('Phonebook_Records', ['Valli','valli009@gmail.com',8394002022,9034758992])



db.print_table('Phonebook_Records')
print("\n")

# Update Syntax
print("Updated row in Table ==>> Name : John , Column : Phone1")
db.update('Phonebook_Records', {'Email': 'smilejohn90@gmail.com'}, {'Name':'John'})
db.print_table('Phonebook_Records')

# Delete syntax
print("\n")
print("Deleted column in Table ==>> Name : Valli")
db.delete_from('Phonebook_Records', {'Name': 'Valli'})
db.print_table('Phonebook_Records')


# In[ ]:


# ********************************************** END *************************************************************************

