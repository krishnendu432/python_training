# Here we will check how to import the another function which is define in another page
import calculator_function_operation_part4 # import the page "calculator_function_operation_part4"

num1=int(input("Enter 1st number to perform the arithematic operation :"))
num2=int(input("Enter 2nd number to perform the arithematic operation :"))
result=calculator_function_operation_part4.add(num1,num2) # call the add() which is define in another page.
print(f"The addition of the number is {result}")
result=calculator_function_operation_part4.mul(num1, num2) # call the mul() which is define in another page.
print(f"The multiplication of the number is {result}")
num3=int(input("Enter the number to check is it odd or even number :"))
result=calculator_function_operation_part4.even_odd(num3) # call the even_odd() which is define in another page.

