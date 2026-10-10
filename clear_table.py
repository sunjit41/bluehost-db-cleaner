import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def delete_old_data():
    try:
        # Connect to BlueHost MySQL Database
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )

        if connection.is_connected():
            cursor = connection.cursor()
            table_name = os.getenv('DB_TABLE')
            date_column = os.getenv('DB_DATE_COLUMN') # e.g., 'created_at' or 'timestamp'
            
            # SQL query to safely target rows older than 24 hours
            query = f"""
                DELETE FROM `{table_name}` 
                WHERE `{date_column}` < NOW() - INTERVAL 1 DAY;
            """
            
            cursor.execute(query)
            connection.commit()
            
            print(f"Success: Cleaned table '{table_name}'. Removed {cursor.rowcount} rows older than 24 hours.")

    except Error as e:
        print(f"Database Error: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection securely closed.")

if __name__ == "__main__":
    delete_old_data()
