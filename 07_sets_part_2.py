# Take the only integer input from the user and print only unique number
number_set=set() #
try:
    number=int(input("Enter how many number you want to take as a input:"))
    count=0
    while count < number :
        digit=input("Enter your input:")
        number_set.add(digit)
        count=count+1
    print(f"The list of the input: {number_set}")
except Exception as e:
    print(e, type(e))
# can we add a same integer number like 18 and the same string value '18' add in the set
my_set=set()
print("Take an same value integer number, float and string from the user and print in sets :")
number=int(input("Enter your integer number:"))
my_set.add(number)
flt=float(input("Enter your float number:"))
my_set.add(flt)
str=input("Enter your string:")
my_set.add(str)
print(f"After perform the addition operation the value of the set is: {my_set}")
# In python the floating point number '18.0' and integer '18' will return the same value if you use the 'comparison operator'.
# Hence, here length will come '2'.
print(f"The length of the set is: {len(my_set)}")
