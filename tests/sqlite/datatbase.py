import sqlite3

# Connect to database
#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Query the database: AND/OR

#c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
#c.execute("SELECT rowid, * FROM customers ORDER BY rowid ASC")
c.execute("SELECT rowid, * FROM customers WHERE first_name LIKE '%a' AND rowid = 3")

items = c.fetchall()
#print(items)
for item in items:
    print(item)

print("!execute!")

# Commit
conn.commit()

# close our connection
conn.close()
