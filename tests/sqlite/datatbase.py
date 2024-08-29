import sqlite3

# Connect to database
#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Query the database
c.execute("SELECT * FROM customers")
#c.fetchone()
#c.fetchmany(3)
print(c.fetchall())

print("execute")

# Commit
conn.commit()

# close our connection
conn.close()
