import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the user table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    email TEXT,
    birthdate TEXT,
    country TEXT
)
''')

# Manually create some sample data
sample_data = [
    (1, 'user1', 'user1@example.com', '1990-01-01', 'USA'),
    (2, 'user2', 'user2@example.com', '1992-02-02', 'Canada'),
    (3, 'user3', 'user3@example.com', '1994-03-03', 'UK'),
]

# Insert the sample data into the user table
cursor.executemany('INSERT INTO users VALUES (?, ?, ?, ?, ?)', sample_data)

# Commit the changes and close the connection
conn.commit()
conn.close()
