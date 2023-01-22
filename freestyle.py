import sqlite3

# CREATING A DATABASE CALLED FLACKO
conn = sqlite3.connect('memory:')
c = conn.cursor()
conn.commit()
# CREATING A TABLE TO INSERT DATA INTO OUR DB
# CREATING A DATABASECALLED FLACKO
c.execute('CREATE TABLE IF NOT EXISTS flacko (name TEXT , age INTEGER, team TEXT , salary INTEGER, position TEXT)')
conn.commit()
flackos = [("Russell Westbrook", 32, "Lakers", 47000000, "PG"),
           ("Lebron James", 36, "Lakers", 39000000, "PF"),
           ("Kyrie Irving", 29, "Nets", 38000000, "PG"),
           ("Dwight Howard", 35, "Taiwan", 280000, "C")]
c.executemany('INSERT INTO flacko VALUES (?,?,?,?,?)',flackos)  # INSERTING DATA INTO OUR DATABASE
conn.commit()

# SELECTING ALL VALUES FROM A TABLE IN OUR DB
c.execute('SELECT * FROM flacko')
data = c.fetchall()  # GETTING OUR DATA USING THE FETCHALL FUNCTION
print("Your initial data : ", data)
