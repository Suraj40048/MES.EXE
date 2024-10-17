import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MySQL connection details from environment variables
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'D252V4L3t8xTC7F'),
    'database': os.getenv('DB_NAME', 'solar')
}

def get_db_connection():
    """Create and return a new database connection."""
    try:
        # Ensure that the connection returns a connection object, not a connection string
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as e:
        print(f"Database connection error: {e}")
        return None
