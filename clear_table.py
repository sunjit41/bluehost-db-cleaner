import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_load  # Loads environment variables from a .env file

# Load environment variables
load_dotenv()

def delete_table_data():
    try:
        # Establish connection using environment variables
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )

        if connection.is_connected():
            cursor = connection.cursor()
            table_name = os.getenv('DB_TABLE')
            
            # Use safe formatting for table names (SQL parameters don't support table names directly)
            query = f"DELETE FROM `{table_name}`;"
            
            cursor.execute(query)
            connection.commit()
            
            print(f"Success: Wiped table '{table_name}'. Rows affected: {cursor.rowcount}")

    except Error as e:
        print(f"Database Error: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection securely closed.")

if __name__ == "__main__":
    delete_table_data()
