import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('input.csv')

# Convert the DataFrame to XLSX
data.to_excel('output.xlsx', index=False)
