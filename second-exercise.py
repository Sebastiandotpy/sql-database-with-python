import sqlite3
import random
import string

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('users2.db')
cursor = conn.cursor()

# Create the user table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT,
    birthdate TEXT,
    country TEXT
)
''')

# Define the number of users you want to generate
num_users = 5

# Generate random data for each user
user_values = []
for i in range(num_users):
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    email = f'{username}@example.com'
    birthdate = f'{random.randint(1970, 2000)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}'
    country = random.choice(['USA', 'Canada', 'UK'])
    user_values.append((username, email, birthdate, country))

# Insert the generated data into the user table
cursor.executemany('INSERT INTO users (username, email, birthdate, country) VALUES (?, ?, ?, ?)', user_values)

# Commit the changes and close the connection
conn.commit()
conn.close()

