# We will check the conditional statement here
# wewill check a given number is even or odd
num1=int(input("Enter any number : "))
if (num1%2==0):
    print(f" This is an Even Number: {num1}")
else:
    print(f"This is an Odd Number {num1}")


# We will check a the name is exist in the list or not
godName=["Mahadev", "Hari", "Durga", "Laxmi", "Ganesh", "Saraswati" ]
#str1=input("Enter the God Name: ")
if 'Hari' in godName:
    print("The condition is true")
else:
    print("The condition is false")

#Now we will check the user list is empty or not
if godName:
#If the list having a single value also, the it will execute 1st condition. Otherwise it will execute false statement.
    print("The list is not empty. The length of the list is :")
    print(godName.__len__())
else:
    print("The list is empty.")