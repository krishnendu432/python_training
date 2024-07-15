# This script we will check how to manage the data.
# We will use pandas package using "Pypi" package manager.
import pandas
# Read the csv file
data=pandas.read_csv('user_details.csv')
print("The content of the .csv file is:-")
print(data)
# We want to get only specific column from the list
print("Display the designation details only :-")
print(data.designation)
print("Display the salary details only :-")
print(data.salary)
print("Find the maximum salary from the list :- ")
print(data.salary.max())
print("Find the minimum salary from the list :- ")
print(data.salary.min())
print("Find the total amount of the salary:-")
print(data.salary.sum())
print("Find the details of the users who is getting salary more than 50000")
print(data[data.salary >= 50000])
print("Find the details of the users whose designation is doctor :-")
print(data[data.designation == 'doctor'])
print("Find the details of the users whose salary is maximum from the list :-")
print(data[data.salary == data.salary.max()])
print("Find the average salary of the users: ")
print(data.salary.mean())
print("Find the full name of the user whose user ID is 11 :")
id_11=data[data.id == 11]
print(id_11.firstname.values[0], id_11.lastname.values[0])
print(" Change the salary column as a list structure  : ")
print(data.salary.to_list())
