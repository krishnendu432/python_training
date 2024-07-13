# We will create our first fuction in python
def mydef(): #we have define the function here
    print("Welcome 2024")
    print("*"*20)
    print("This is my 1st program for python" )
# We will call the fuction 3 time
mydef()
mydef()
mydef()


# We will create another function
def welcome_note(user_name,user_age=none) : # Define a function with a single parameter
#If some one don't know its age or not provided age the it will print none at the place of age
    print("*********************")
    print(f"Welcome {user_name} to our city")
    print(f"Age of the user is: {user_age}")#End of the function
count=int(input("For how many users you want to create welcome note : "))
i=0
while i<count : #create a while loop and it will continue untill how many users you want to print
    my_user = input("Please enter the user name :")
    age=int(input("Enter the age of the user : "))
    welcome_note(my_user,age) #call to the user
    i=i+1

