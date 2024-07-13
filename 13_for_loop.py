# This script we will check the for loop script
for i in 10, 20, 30, 40, 60:
    print(f" The values are {i}")
    print("This is my first for loop script in Python")
# How to print a range using for loop
for i in range(10,20):
    print("Print the given range")
    print(i)

# How to use for loop in list
team_list = ["Jaisawal", "Gill", "Hardik", "Surya", "Mukesh"]
for user in team_list:
    print(f"The team members are {user}")
# How to use for loop in dictionary
team_score = { "Jaisawal" : 55,
               "Gill" : 35,
               "Hardik" : 49,
               "Surya" : 78,
               "Mukesh" : 15}
for key, value in team_score.items() :
# In dictionary to fetch the value useing for loop use .items() with the diecionary name
    print(f" The name of the player is: {key} ")
    print(f" The score did by the {key}: {value}")
# Suppose we need only name from the dictionary then we can do
for name in team_score.keys() :
    print(f" The name of the player is: {name} ")
# If you need to be get the value then use below code
for run in team_score.values() :
    print(f" The name of the player is: {run} ")
# Print from minimum number to maximum number given by the user.
max1= int(input("Enter your maximum value : "))
min1 = int(input("Enter your minimum value : "))
j=min1
for j in range(min1,max1+1):
   print(f" Print the value from min to max {j}")
