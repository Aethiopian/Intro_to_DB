import mysql.connector
from mysql.connector import errorcode

def create_database():
    # Connection settings
    config = {
        'user': 'root',  # replace with your MySQL username
        'password': 'tooras2024',  # replace with your MySQL password
        'host': 'localhost',  # assuming local MySQL server
        'raise_on_warnings': True
    }

    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        # Attempt to create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Incorrect username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist")
        else:
            print(f"Error: {err}")
    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    create_database()
