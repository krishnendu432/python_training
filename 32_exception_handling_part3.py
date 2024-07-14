# this is the code to perform the exception handling
print("To perform the division operation your 1st number should be higher than 2nd number")
try :
    num1=int(input("Enter any number to perform the operation: "))
    num2=int(input("Enter any number to perform the operation: "))
    if num1 > num2:
        div = num1 / num2
        print(f"The result of the operation is: {int(div)}")
    else:
        print("The 1st number should be higher than 2nd number other wise it will not give any result")
except Exception as e: # If you don't know what exact exception will come then used general exception block
    print(e, type(e))
# This end portion of the operation has been used for testing purpose that exception block is working properly or not.
print("Hello")
