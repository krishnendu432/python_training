# We will create another function
# Dynamic argument function
# the dynamic argument should be in the last argument, we can't define it normal variable after argument.
def welcome_note(user_name,**user_info) : # Define a function with a dynamic parameters, apart from user name all are dynamic parameters
# if user having multiple hobbies then after two parameters all the value it will calculate the value of parameter three
#If some one don't know its age or not provided age the it will print none at the place of age
    print("*********************")
    print(f"Welcome {user_name} to our city")
    print("User's other information are: ")#It will print the bobbies as a list
    for key, value in user_info.items() : # It will print the value as a dictionary
        print(f"- {key} is {value}") #created tupple as a output
#End of the function
count=int(input("For how many users you want to create welcome note : "))
i=0
while i<count : #create a while loop and it will continue untill how many users you want to print
    my_user = input("Please enter the user name :")
    age=int(input("Enter the age of the user : "))
    contact_num=int(input("Enter the contact number of the user : "))
    email=input("Enter the email ID : ")
#Here we will passes the details as a dynamic arguments, in this case user may not provide all the information also
    welcome_note(my_user,age=age,contact_num=contact_num, email=email) #call to the user
    i=i+1
