import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
# All data based on a condition
cursor.execute("SELECT * FROM events WHERE band='Dire Straits'")
rows = cursor.fetchall()
print(rows)

# Query columns on condition
cursor.execute(
    "SELECT band, date FROM events WHERE date='08 24 1987'")
rows = cursor.fetchall()
print(rows)
"""
returns
[('Dire Straits', 'Toronto', '08 24 1972')]
[('Eric Clapton', '08 24 1987')]
"""

# Insert rows
new_rows = [('Jeff Beck', 'Buffalo', '08 24 2013'),
            ('Eric Johnson', 'Rochester', '06 14 2023')]
cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

# Get all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)
