# -*- coding: utf-8 -*-
"""Olympics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P8UV2gou0j_c4CYlUXkTAdbJ94iHAN0c
"""

import psycopg2
import pandas as pd

# Replace the following connection string with your actual database URL
db_url = "postgres://student:tAdJApZJw7X3C%40xs@ep-noisy-flower-846766.us-east-2.aws.neon.tech/olympics"

try:
    # Establish a connection to the PostgreSQL server using the URL
    connection = psycopg2.connect(db_url)

    # Create a cursor to interact with the database
    cursor = connection.cursor()

    # Execute SQL queries
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print("Connected to PostgreSQL version:", version)

    cursor.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)

# Create a cursor to interact with the database
cursor = connection.cursor()

# Execute SQL query to select data from the database
query = "SELECT * FROM athletes_events;"
cursor.execute(query)

# Fetch all the selected data into a list of tuples
data = cursor.fetchall()

# Get column names from the cursor description
column_names = [desc[0] for desc in cursor.description]

# Define the data types for each column in a dictionary
dtype_mapping = {
    'weight': 'float'
}

# Create a Pandas DataFrame from the selected data and column names with specified data types
df = pd.DataFrame(data, columns=column_names).astype(dtype_mapping)

# Don't forget to close the cursor and the connection
cursor.close()
connection.close()

df.head()

# Create a new dataframe called "summer_games_df" that filters Summer games.

summer_games_df = df[df['season'] == "Summer"]
summer_games_df

# Subset this new dataframe to only include the following columns: name, teams, games, sport and medal
summer_games_df_subset = summer_games_df[['name', 'team', 'games', 'sport', 'medal']]
summer_games_df_subset

# Create a new df, china_gold_df, that subsets summer_games_df by the teams from China where a gold medal was won
china_df = summer_games_df_subset[summer_games_df_subset['team'] == "China"]
china_gold_df = china_df[china_df['medal'] == "Gold"]
china_gold_df

# what sports has Namibia competed in?
namibia_df = summer_games_df_subset[summer_games_df_subset['team'] == "Namibia"]
namibia_df['sport'].unique()

# create a new dataframe, clean_df, that cleans up team names (China-1 -> China, China-2 -> China. China-3 -> China)
clean_df['team'] = df['team'].str.replace(r'\d+', '', regex=True).unique()
clean_df = pd.DataFrame({'team': clean_df['team']})
clean_df