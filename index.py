
# import panda library
import pandas as pd

# read excel file
project_details = pd.read_excel('project_details.xlsx')
# employee_salary = pd.read_excel('employee_salary.xlsx')

# print excel sheet data
print('\n')
print(' ----- Printing excel sheet data -----')
print(project_details)

# print only specifix columns
print('\n')
print('Print only specific columns')
print(project_details[['Status', 'Project Name']])

# showing top 5 rows
print('\n')
print(' ----- Printing top 5 rows -----')
print(project_details.head())

# showing bottom 5 rows
print('\n')
print(' ----- Printing bottom 5 rows -----')
print(project_details.tail())

# sort data
sorted_column = project_details.sort_values(['Status'], ascending = True)

print('\n')
print(' ----- Printing sorted data -----')
print(sorted_column)



