import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import shutil

# Create a sample DataFrame
data = {
    'Column1': ['A', 'B', 'C', 'D', 'E'],
    'Column2': ['a', 'b', 'a', 'c', 'a'],
    'a': [1, 2, 3, 4, 5],
    'b': [5, 4, 3, 2, 1],
    'Category': ['X', 'Y', 'X', 'Y', 'X'],
    'Attribute': ['W', 'X', 'Y', 'Z', 'W'],
    'Value': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# .loc: select rows and columns by labels
# Change 'Column1' to 'NewValue' where 'Column2' is 'a'
df.loc[df['Column2'] == 'a', 'Column1'] = 'NewValue'
# Select value at row 3, column 'a'
value = df.loc[3, 'a']
print(value)

# .iloc: select rows and columns by position
# Select value at row 3, column with positional index of 'a'
value = df.iloc[3, df.columns.get_loc('a')]
print(value)
# Select the first 4 columns and the last column of the DataFrame
p1 = df.iloc[:, [0, 1, 2, 3, -1]]
# Select from the 4th column to the end
p2 = df.iloc[:, 4:]

# Concatenate DataFrames: add a new row
new_row = pd.DataFrame({'Column1': ['F'], 'Column2': ['d'], 'a': [6], 'b': [0], 'Category': ['Z'], 'Attribute': ['V'], 'Value': [60]})
df = pd.concat([df, new_row], ignore_index=True)

# Sort values
# Sort DataFrame by 'Column1' ascending and 'a' descending
df.sort_values(by=['Column1', 'a'], ascending=[True, False], inplace=True)

# Drop duplicates
# Remove duplicates based on 'Column1', keeping the first occurrence
df.drop_duplicates(subset=['Column1'], keep='first', inplace=True)

# Drop columns
# Remove columns 'a' and 'b'
df.drop(['a', 'b'], axis=1, inplace=True)

# Rename columns
# Rename 'Value' to 'Value_sum'
df.rename(columns={'Value': 'Value_sum'}, inplace=True)

# Group and aggregate
# Group by 'Category' and 'Attribute', and calculate the sum of 'Value_sum'
grouped_df = df.groupby(['Category', 'Attribute'], as_index=False).agg({'Value_sum': 'sum'})

# Fill missing values
# Fill NaN in 'Value_sum' with 0
df['Value_sum'].fillna(0, inplace=True)

# Calculate ranks
# Create a rank column based on 'Value_sum'
df['rank'] = df['Value_sum'].rank()

# Apply lambda function
# Create a column with the length of 'Column1'
df['largo'] = df['Column1'].apply(lambda x: len(x))

# Create a pivot table
pivot_df = df.pivot_table(index='Category', columns='Attribute', values='Value_sum', aggfunc='sum')

# Iterate with enumerate
for h, g in enumerate(df['Column1']):
    if h < 3:
        print(g)  # Print the first 3 elements
    if h > 3:
        break  # Stop the loop after the fourth element

# Use continue in loop
for element in df['Column1']:
    if element == 'B':
        continue  # Skip the element 'B'
    print(element)

# Range of numbers
rango = range(5)
print(list(rango))  # Prints [0, 1, 2, 3, 4]

rango2 = range(2, 9, 2)
print(list(rango2))  # Prints [2, 4, 6, 8]

# Iterate over multiple lists
names = ['John', 'Jane']
surnames = ['Doe', 'Smith']
for name, surname in zip(names, surnames):
    print(name, surname)

# List comprehension
lista = [2, 4, 6]
list_comprehension = [num**2 for num in lista]
list_comprehension3 = [num**2 if num != 4 else (num+1)**2 for num in lista]

# Use of *args
def sum_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result

# Formatted string with f-strings
run_id = '1234'
rmse = 0.5678
print(f"run id: {run_id}, rmse: {rmse:.4f}")

month = 2
print(f"{month:02d}")

# Measure execution time
from datetime import datetime
start_time = datetime.now()
# Code whose execution is measured
end_time = datetime.now()
duration = end_time - start_time
duration_in_seconds = float(duration.total_seconds())

# Iterate over files in a directory
import os
path = '/path/to/directory'
for file in os.listdir(path):
    if file.endswith('.xlsx'):
        # Process Excel file
        print(file)


# Use of map and zip
def square(number):
    return number**2

lista = [2, 4, 6]
map_square = map(square, lista)
print(list(map_square))

# Clustering with KMeans
X = df[['Value_sum']]
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
df['cluster'] = kmeans.labels_

# Filter with conditions
conditions = [
    df['Column2'].str.upper().isin(['A', 'B']),
    df['Column2'].str.upper().isin(['C', 'D'])
]
choices = ['Group1', 'Group2']
df['Group'] = np.select(conditions, choices, default='Other')
print(df)

# Format Excel file
excel_writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
df.to_excel(excel_writer, sheet_name='Sheet1', index=False)
worksheet = excel_writer.sheets['Sheet1']
worksheet.autofilter('A1:F1')
worksheet.freeze_panes(1, 0)
num_format = workbook.add_format({'num_format': '#,##0.00'})
percent_format = workbook.add_format({'num_format': '0.00%'})
worksheet.set_column('A:F', 20, num_format)
worksheet.set_column('C:C', 20, percent_format)
excel_writer.save()

# Save DataFrame to gzip file
df.to_csv('data.csv.gz', compression='gzip', index=False)

# Read DataFrame from compressed parquet file
df = pd.read_parquet('data.parquet.gzip')

# SQL queries and data manipulation
import pyodbc
db_connection = pyodbc.connect('Driver={SQL Server};Server=servername;Database=database_name;Trusted_Connection=yes;')
db_cursor = db_connection.cursor()

# Execute SQL query
query = "SELECT * FROM my_table"
df_sql = pd.read_sql(query, db_connection)
