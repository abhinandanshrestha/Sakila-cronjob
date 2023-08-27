import mysql.connector
from dotenv import load_dotenv
import os
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# MySQL Database Configuration
db_config = {
    'user': os.getenv('user'),
    'password': os.getenv('password'),
    'host': os.getenv('host'),
    'database': os.getenv('database')
}

# Fetch new rentals in the last 1 hour
query = """
    SELECT
        r.rental_id,
        r.rental_date,
        CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
        f.title AS film_title,
        co.country AS customer_country
    FROM rental r
    JOIN customer c ON r.customer_id = c.customer_id
    JOIN inventory i ON r.inventory_id = i.inventory_id
    JOIN film f ON i.film_id = f.film_id
    JOIN address a ON c.address_id = a.address_id
    JOIN city ci ON a.city_id = ci.city_id
    JOIN country co ON ci.country_id = co.country_id
    WHERE r.rental_date >= NOW() - INTERVAL 1 HOUR
"""

def getResult():

    try:

        # Attempt to connect to the database
        db_conn = mysql.connector.connect(**db_config)
        cursor = db_conn.cursor()

        # Execute the query
        cursor.execute(query)
        
        # Fetch the results
        result = cursor.fetchall()

        # Create a DataFrame from the query result
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(result, columns=columns)

        return df

    except mysql.connector.Error as err:

        # Handle the exception if a MySQL error occurs
        print("MySQL Error:", err)

    finally:
        
        # Make sure to close the database connection in all cases
        if 'db_conn' in locals() and db_conn.is_connected():
            cursor.close()
            db_conn.close()
            print("Database connection closed.")
