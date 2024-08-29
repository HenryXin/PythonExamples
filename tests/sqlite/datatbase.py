import sqlite3

# Connect to database
#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Query the database
c.execute("SELECT * FROM customers")
#print(c.fetchone())
#print(c.fetchone()[0])
#print(c.fetchmany(3))
#print(c.fetchall())

items = c.fetchall()
#print(items)

print("NAME\t\t" + "EMAIL")
print("----------------------------------------")
for item in items:
    print(item[0] +"."+ item[1]+"\t|"+item[2])

print("!execute!")

# Commit
conn.commit()

# close our connection
conn.close()
