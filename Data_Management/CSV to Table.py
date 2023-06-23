import pandas as pd
from tabulate import tabulate

# Load the CSV file into a DataFrame
data = pd.read_csv("records.csv")

# Display the DataFrame as a table
print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
