import mysql.connector
import pandas as pd
import numpy as np

# Taking user input for login 
user_id = input("Enter MySQL user ID: ")
password = input("Enter MySQL password: ")
database = input("Enter the database name: ")

try:
    # Establishing connection
    Database = mysql.connector.connect(
        host="localhost", 
        user=user_id,
        password=password,
        database=database
    )

    if Database.is_connected():
        print("Connected successfully")
        mycursor = Database.cursor()  

        # Query execution
        query = "SELECT * FROM actor"
        mycursor.execute(query)  
        
        # Fetching and printing the result
        result = mycursor.fetchall()
        for row in result:
            print(row)
    else:
        print("Not connected!!!")

except mysql.connector.Error as err:
    # Handling any connection errors
    print(f"Error: {err}")

finally:
    # Ensuring the connection is closed after execution
    if Database.is_connected():
        mycursor.close()
        Database.close()
        print("MySQL connection closed.")
