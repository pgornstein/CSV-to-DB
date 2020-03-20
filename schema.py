import sqlite3
import os

PATH = os.path.dirname(__file__)
DATAPATH = os.path.join(PATH, "employees.db")

def create_tables(dbpath=DATAPATH):
    with sqlite3.connect(dbpath) as connection:
        curs = connection.cursor()
        #If exists, drop user table
        sql = "DROP TABLE IF EXISTS users"
        curs.execute(sql)
        #If exists, drop phone table
        sql = "DROP TABLE IF EXISTS phone_numbers"
        curs.execute(sql)
        #Create user table
        sql = """CREATE TABLE users (
                 name VARCHAR(50) PRIMARY KEY,
                 email VARCHAR(100),
                 country VARCHAR(30)
                );"""
        curs.execute(sql)
        #Create phone table
        sql = """CREATE TABLE phone_numbers (
                 phone_number VARCHAR(12) PRIMARY KEY,
                 name VARCHAR(50),
                 type VARCHAR(5)
                );"""
        curs.execute(sql)