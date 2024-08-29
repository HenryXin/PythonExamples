import sqlite3

# Connect to database
#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

customers_list = [('Dorothy', 'Agular', 'DAgular@test.com'),
             ('Arman', 'Beltran', 'ABeltran@testing.com'),
             ('Eshal', 'Blaese', 'EBlaese@gmail.com')]

# insert records
c.executemany("INSERT INTO customers VALUES (?,?,?)", customers_list)

# NULL
# INTEGER
# REAL
# TEXT
# BLOG

print("Insert records")

# Commit
conn.commit()

# close our connection
conn.close()
