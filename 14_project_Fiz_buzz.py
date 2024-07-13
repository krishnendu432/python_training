# Write a program where user will give the minimum and maximum range for a list.
# With in the user's given range if the value is multiply by 3 then type fizz in the list
# If the value is multiply by 5 then type buzz in the list
# If the value is multiply by both 3 and 5 then type fizz buzz
min1=int(input("Enter your minimum value : "))
max1=int(input("Enter your maximum value : "))
# Created a blank list
my_list=[]
# assign min value to i variable
i=min1
for i in range(min1,max1+1):
# create a new variable result and assign "" to the result variable.
    result=""
    if i % 3 == 0 :
        result=result+"Fizz"
        if i % 5 == 0:
            result = result + "Buzz"
#concate the string between "Fizz" and result variable
    elif i % 5 == 0:
        result=result+"Buzz"
    else:
        result=i
#concate the string between "Buzz" and result variable
# Append the value to the particular list
    my_list.append(result)
    #my_list.append(i)
print(my_list)
