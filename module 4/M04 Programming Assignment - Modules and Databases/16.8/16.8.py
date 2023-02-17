# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:33:27 2023

@author: Kyle Stitt

sdev 245 Spring 2023
"""

import sqlite3

conn = sqlite3.connect("books.db")
cur = conn.cursor()

#cur.execute('CREATE TABLE books(title, author, year)')

#cur.execute("INSERT INTO books VALUES ('Hunger Games', 'Susan Collins', 2014)")

cur.execute("SELECT * FROM books WHERE title='Hunger Games'")

print(cur.fetchone())
conn.commit()

conn.close()