import sqlite3

# Connect to database
#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Drop a table

c.execute("DROP TABLE customers")
conn.commit()
c.execute("SELECT * FROM customers")
items = c.fetchall()
#print(items)
for item in items:
    print(item)

print("!execute!")

# Commit
conn.commit()

# close our connection
conn.close()
