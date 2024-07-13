# we will check a given number is even or odd using while loop
user_input=""
# Create a initial condition it will work till to user press "q"
while user_input != 'q':
    user_input = input("Enter any number or press 'q' to quit : ")
    if user_input.isdigit():
# It will retun true value if the user value is numeric string other wise false
        if (int(user_input) % 2 == 0):
            print(f" This is an Even Number: {user_input}")
        else:
            print(f"This is an Odd Number {user_input}")

