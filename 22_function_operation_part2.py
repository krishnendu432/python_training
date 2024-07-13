# We will create another function
# Dynamic argument function
def welcome_note(user_name,user_age,*user_hobbies) : # Define a function with a three parameters,
# if user having multiple hobbies then after two parameters all the value it will calculate the value of parameter three
#If some one don't know its age or not provided age the it will print none at the place of age
    print("*********************")
    print(f"Welcome {user_name} to our city")
    print(f"Age of the user is: {user_age}")
    print("User's hobbies are: ")#It will print the bobbies as a list
    for hobby in user_hobbies :
        print(f"- {hobby}") #created tupple as a output
#End of the function
count=int(input("For how many users you want to create welcome note : "))
i=0
while i<count : #create a while loop and it will continue untill how many users you want to print
    my_user = input("Please enter the user name :")
    age=int(input("Enter the age of the user : "))
    hoby=input("Enter the hobbies user : ")
    welcome_note(my_user,age,hoby) #call to the user
    i=i+1
