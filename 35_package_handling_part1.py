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
print("display the csv file as a dictionary format :")
print(data.to_dict())
print("Update the salary 75000 of the user whose user id is 15")
data.loc[data.id == 15, 'salary'] = 75000
print(data)
print("Sort the user list basis of salary in ascending ordered :")
data=data.sort_values(by='salary', ascending=True)
print(data)
print("Added a new column incremented_salary and giving the 10% salary hike on their present salary :")
data['incremented_salary']=data.salary*.10
print(data)
data['salary']=data.salary+data.incremented_salary
print("New salary is after adding incremented_salary :")
# After calculate the new salary removed 'incremented_salary' column
data=data.drop('incremented_salary', axis=1)
print(data)
print("Remove the information of user ID:-16")
print("Before remove the data of user ID 16, please check the details of the user :")
id_16=data[data.id == 16]
print(id_16)
user_ID=data.index[data.id == 16].to_list()[0]
data=data.drop(user_ID)
print("After removed the data the user information is:- ")
print(data)
print("Save the new data information permanently in modified file and display it: ")
data.to_csv('user_details_modified')
modified_data=pandas.read_csv('user_details_modified')
print(modified_data)

