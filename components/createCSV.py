import os
import pandas as pd

# Define the CSV filename
csv_filename = '/home/abhi/Sakila Project/CSV/new_rentals.csv'

def createCSV(rentals_df):
    # Remove the existing CSV file if it exists
    if os.path.exists(csv_filename):
        os.remove(csv_filename)

    # Save the DataFrame to a new CSV file
    rentals_df.to_csv(csv_filename, index=False)

    print(f"CSV file '{csv_filename}' created successfully.")