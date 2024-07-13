# This is for nested if else statement
age=int(input("Enter your age :"))
#print("Do you have voter card. Answer by only TRUE or FALSE")
#voterCard=input()
voterCard=True
if age > 18 :
    if voterCard:
        print(f"You are eligible for giving vote: age is {age}")
    else:
        print(f"You should apply for the voter id card {age}.")
else:
    print(f"Youare not eligible for giving vote {age}")
