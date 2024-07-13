# How to add two strings
F_Name = "Narandra"
L_Name = "Modi"
F_Name = " " + F_Name + " " + L_Name
print(f"Name of our Prime Minister is :{F_Name}")
# Different String Operations
# Need full value in Upper case letter
print(F_Name.upper())

# Need full value in Lower case letter
print(F_Name.lower())

str1= "Mr. narandra modi is our prime minister from 2014"
# How to use split program
print(str1.split())
# If we need to split a after a specific symbol or word then also you can use split
print(str1.split("our"))
# How to use title program
print(str1.title())
# How to retrive specific value from string
print(str1[0])
# How to retrive specific words from the string along with title format
print(str1[0:18].title())
# If you required the word from end of the line then also you can use '-' indexing
print(str1[-1])

