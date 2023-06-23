import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('records.csv')

# Convert the DataFrame to XLSX
data.to_excel('output.xlsx', index=False)
