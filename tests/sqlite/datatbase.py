import sqlite3

# Connect to database
#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Update Records

c.execute("""UPDATE customers SET first_name = 'Dorothy'
WHERE rowid = 4
""")
conn.commit()

c.execute("SELECT rowid, * FROM customers")
#c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE '%r'")
#print(c.fetchone())
#print(c.fetchone()[0])
#print(c.fetchmany(3))
#print(c.fetchall())

items = c.fetchall()
#print(items)
for item in items:
    print(item)

print("!execute!")

# Commit
conn.commit()

# close our connection
conn.close()
