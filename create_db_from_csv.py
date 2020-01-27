import csv
import sqlite3

#get data from csv file
with open('employees.csv', newline= '') as f_object:
    data = [row for row in csv.reader(f_object)]
    users_data = [[row[0], row[4], row[5]] for row in data]
    phone_numbers_data = [row[1:4] for row in data]

#Connect to database
with sqlite3.connect('employees.db') as connection:
    cursor = connection.cursor()

    employees = """DROP TABLE IF EXISTS employees"""
    cursor.execute(employees)

    #Create table employees that takes ALL the data from csv
    employees = """CREATE TABLE employees (
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(32),
        cellphone CHAR(12),
        homephone CHAR(12),
        workphone CHAR(12),
        email VARCHAR(50),
        country VARCHAR(20)
        );"""
    cursor.execute(employees)

    #some of the rows have 7 columns rather than 6
    s = slice(6)

    for row in data:

        cursor.execute(f"""INSERT INTO employees (
            name, cellphone, homephone, workphone, email, country
            ) VALUES (
            ?,?,?,?,?,?);""", row[s])
        
        #OperationalError: no such column: name
        # cursor.execute(f"""INSERT INTO employees (
        #     name, cellphone, homephone, workphone, email, country
        #     ) VALUES (
        #     {row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]});""")
    connection.commit()

#Create table users that takes user data except phone numbers
with sqlite3.connect('users.db') as connection:
    cursor = connection.cursor()

    users = """DROP TABLE IF EXISTS users"""
    cursor.execute(users)

    users = """CREATE TABLE users (
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(32),
        email VARCHAR(50),
        country VARCHAR(50)
        );"""
    cursor.execute(users)

    for row in users_data:

        cursor.execute(f"""INSERT INTO users (
                name, email, country
                ) VALUES (
                ?,?,?);""", row)
    connection.commit()

#Create table phone_number that takes phone number data
with sqlite3.connect('phone_numbers.db') as connection:
    cursor = connection.cursor()

    phone_numbers = """DROP TABLE IF EXISTS phone_numbers"""
    cursor.execute(phone_numbers)

    phone_numbers = """CREATE TABLE phone_numbers (
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        cellphone CHAR(12),
        homephone CHAR(12),
        workphone CHAR(12)
        );"""
    cursor.execute(phone_numbers)

    for row in phone_numbers_data:

        cursor.execute("""INSERT INTO phone_numbers (
                cellphone, homephone, workphone
                ) VALUES (
                ?,?,?);""", row)
    connection.commit()

with sqlite3.connect('users.db') as connection:
    cursor = connection.cursor()

    cursor.execute("""SELECT name FROM users WHERE country == "Grenada" """)
    live_in_grenda = cursor.fetchall()

    cursor.execute("""SELECT name FROM users WHERE country == "Korea" """)
    live_in_korea = cursor.fetchall()

    cursor.execute("""SELECT name FROM users WHERE name LIKE "%cindy%" """)
    cindy = cursor.fetchall()

#People who live in Grenada
"""Jimmy Hendricks
Ginger Noble
Stefanie Dunn"""

#People who live in Korea
"""Marian Mcpherson
Chas Coffey
Felipe Lozano
Marianne Chase
Rosella Adams
Richard Hinton
Duncan Sandoval"""

#People whose full name contain the name Cindy
#SELECT name FROM users WHERE name LIKE "%cindy%"
"""Cindy John"""