import pandas as pd
from io import StringIO

# Sample CSV content
csv_data = """Name,Age,Department,Salary
John,28,Sales,50000
Jane,34,Marketing,60000
Doe,45,HR,55000
Alice,30,IT,70000
Bob,50,Sales,80000
Charlie,32,IT,75000
Eve,29,Marketing,72000
Frank,33,HR,48000"""

# Load the CSV data into a DataFrame
df = pd.read_csv(StringIO(csv_data))

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Filter the data to include only employees from the IT department
it_department = df[df['Department'] == 'IT']
print("\nEmployees from IT Department:")
print(it_department)

# Group the data by department and calculate the average salary
average_salary_by_department = df.groupby('Department')['Salary'].mean()
print("\nAverage Salary by Department:")
print(average_salary_by_department)
