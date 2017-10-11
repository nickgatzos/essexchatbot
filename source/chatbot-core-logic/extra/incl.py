import sqlite3

# Database Connection
db = sqlite3.connect('dbconvlog.sqlite3')
cursor = db.cursor()