# Represent a Dice game between 1 to 6
import random
print("Game start !!!!!!!!!!")
while True :
    # random.randint() is a pre define function.
    print(f" Your value is : {random.randint(1,6)}") # Generate the random value between 1 to 6
    user_choice=input(("Enter your choice: If you want to continue press 'y' or if you want to close press 'n':"))
    if user_choice.lower() == 'y':
        continue
    elif user_choice.lower() == 'n':
        print("Gave is over")
        break
    else :
        print("You have enter the wrong input")
        break




