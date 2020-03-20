import csv
import sqlite3
import os
import schema

PATH = os.path.dirname(__file__)
CSVPATH = os.path.join(PATH, "employees.csv")
DATAPATH = os.path.join(PATH, "employees.db")

def insert_user(values, dbpath=DATAPATH):
    with sqlite3.connect(dbpath) as connection:
        curs = connection.cursor()
        sql = """INSERT INTO users (
                 name, email, country
                 ) VALUES (?, ?, ?);"""
        curs.execute(sql, values)

def insert_phone_number(values, dbpath=DATAPATH):
    with sqlite3.connect(dbpath) as connection:
        curs = connection.cursor()
        sql = """INSERT INTO phone_numbers (
                 phone_number, name, type
                 ) VALUES (?, ?, ?);"""
        curs.execute(sql, values)

def import_csv_to_db(csvpath = CSVPATH):
    schema.create_tables()
    with open(csvpath, 'r') as file_object:
        reader = csv.DictReader(file_object)
        for row in reader:
            insert_user((row["name"], row["email"], row["country"]))
            insert_phone_number((row["cellphone"], row["name"], "cell"))
            insert_phone_number((row["homephone"], row["name"], "home"))
            insert_phone_number((row["workphone"], row["name"], "work"))

import_csv_to_db()