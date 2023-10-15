import pandas as pd
from datetime import datetime
from dateutil import parser

# Load the CSV file into a DataFrame
df = pd.read_csv('data job posts.csv')

# Generate unique JobID values
job_id_values = range(1, len(df) + 1)

# Add the JobID column to the DataFrame
df['JobID'] = job_id_values

# Save the DataFrame to a new CSV file with the JobID column
df.to_csv('data_job_posts_modified.csv', index=False)


import pandas as pd
from datetime import datetime

# Input CSV file path
csv_file_path = "data_job_posts_modified.csv"

# Output CSV file path to save the converted data
output_csv_file_path = "data_job_posts_modified.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Specify the name of the date field in your CSV
date_field_name = ["date","StartDate","OpeningDate","Deadline"]

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
df = df.drop(columns=date_field_name)

    # Save the DataFrame to a new CSV file without the date field
df.to_csv(output_csv_file_path, index=False)
