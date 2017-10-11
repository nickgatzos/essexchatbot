import sqlite3

#  Goodbye list
goodbye = ['goodbye', 'bye', 'see you', 'see you soon', 'cya', 'bb', 'ttyl']


# Connection to database
db = sqlite3.connect('dbconvlog.sqlite3')
cursor = db.cursor()
