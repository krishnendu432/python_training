# For loop further operation
marks=[58, 61, 93, 87, 78, 54]
print(f"Display the list {marks}")
# built a for loop and print the list
count =0
length=len(marks)
for count in range(length) :
    print(f"The marks of the student is : {marks[count]}")
    count=count+1

# Take the input from min and max value from the user and print the value from min to max with 4 interval.
min= int(input("Enter the minimum number from where you want to display the number: "))
max= int(input("Enter the maximum number upto how much you want to display the number: "))
count=min
if min < max :
    for count in range(min, max+1, 4) :
        print(f"The value will display from min to max with 4 intervals: {count}")
        count=count+4
else:
    print(f"The max value is less than min value: min :{min} and max :{max}. Hence the operation is not possible.")



