#this is the code to perform the exception handling
num1=float(input("Enter the 1st number to perform the devision operation:"))
num2=float(input("Enter the 2nd number to perform the devision operation:"))
if num1 > num2 :
    try:
        div=(num1/num2)
        print(f"The result of the operation is: {int(div)}")
    except ZeroDivisionError :
        print("Kindly do not devide by zero")
else:
    print(f"1st number should be higher then 2nd number. Otherwise division result will come 0")