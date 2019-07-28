#standard imports
import sqlite3

conn = sqlite3.connect('profiles.db')
conn.execute("CREATE TABLE users (user_id INTEGER, lifetime_pts INTEGER, available_pts INTEGER, UNIQUE(user_id))")