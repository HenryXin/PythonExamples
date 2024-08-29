import sqlite3

# Connect to database
#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# insert a record
#c.execute("""INSERT INTO customers VALUES (
#'Marwa', 'Fowler', 'MFowler@tests.com'
#   )
#""")

#c.execute("INSERT INTO customers VALUES ('Alyssia', 'Phelps', 'APhelps@testing.com')")

c.execute("INSERT INTO customers VALUES ('Vanessa', 'Cantu', 'VCantu@hotmail.com')")

# NULL
# INTEGER
# REAL
# TEXT
# BLOG

print("Insert one record")

# Commit
conn.commit()

# close our connection
conn.close()
