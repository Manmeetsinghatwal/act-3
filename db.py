import mysql.connector
from mysql.connector import Error

def create_connection():
    """Connect to the MySQL Database"""
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='currentapipass',
            database='BTP405'
        )
        print("Successful connection to MySQL database")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection
