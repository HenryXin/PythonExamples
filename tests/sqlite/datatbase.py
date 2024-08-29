import sqlite3

# Connect to database
#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE customers (
   first_name text,
   last_name text,
   email text
   )
""")

# NULL
# INTEGER
# REAL
# TEXT
# BLOG

# Commit
conn.commit()

# close our connection
conn.close()
