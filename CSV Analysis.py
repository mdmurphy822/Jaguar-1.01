import pandas as pd
import numpy as np

# We can take specific data variables and search for their highest or
# lowest values.

# Ask the user for the path
file_path = input("Please enter the file path: ")

# Open the file using pandas
df = pd.read_csv(file_path)

# Get the values from the first row and first column
row_1 = df.iloc[0]
col_1 = row_1.iloc[0]

# Create variables and assign values based on the row and column values
var1 = row_1[col_1]
var2 = row_1[col_1 + "_2"]
var3 = row_1[col_1 + "_3"]

# Find the maximum value in the DataFrame
max_value = df.max().max()

# Find the index of the maximum value
max_index = df[df == max_value].stack().index.get_level_values(1).tolist()[0]

# Find the associated variable
if max_index in df.columns:
    max_var = df[max_index].max()
else:
    max_var = df.iloc[:, df.columns.get_loc(max_index)].max()

# Print the maximum value and the associated variable
print(f"Maximum value: {max_value}")
print(f"Associated variable: {max_var}")