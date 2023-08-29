# sql-database-with-python


*Exercise: Creating a User Table with Faker Data*
Create a data.sql file that generates a user table with 5 different columns using the Faker module in Python. The user table should have the following columns:
1. id (integer) - Primary key for the user.
2. username (string) - A randomly generated username.
3. email (string) - A randomly generated email address.
4. birthdate (date) - A randomly generated birthdate. Use the formate Year-Month-Day.
5. country (string) - A randomly generated country name.
Your task is to use the Faker module to generate random data for each of these columns and write SQL statements to create the user table and insert the generated data.
*Hints:*
1. Import the Faker class from the faker module.
2. Create an instance of the Faker class.
3. Use the instance to generate random values for each column.
4. Write an SQL statement to create the user table with the specified columns.
5. Write an SQL query to insert the generated data into the user table.

*Exercise: Creating a User Table with Faker Data Using sqlite3*
*Instructions:*
1. Import the necessary modules: sqlite3 for working with SQLite databases and Faker for generating fake data.
2. Create a Faker instance to generate random data.
3. Generate random data for the user table columns: username, email, birthdate, and country.
4. Define the number of users you want to generate (num_users).
5. Create an empty list (user_values) to store the generated user data.
