# This script is for how to take input from user
userName=input("Enter your name :")
print(userName)
# Perform string concatenation of two string values
str1=input("Enter your first name :")
print(f"Your First name is: {str1}")

str2=input("Enter your last name :")
print(f"Your last name is: {str2}")
fullName=str1+ " " +str2
print("Your full name is :")
print(fullName)

#Perform numeric operation of given numbers
print("Enter the details of the students:")
print("Enter the marks for the Maths :")
# How to convert a by default string value to interger value
math=int(input())
eng=int(input("Enter the marks for the English :"))
science=int(input("Enter the marks for the Science :"))
com=int(input("Enter the marks for the Computer :"))
total=math+eng+science+com
print(f"Total marks of the student is {total}")
# How to convert a by default string value to float value
print("Enter the details of the runners:")
print("Enter the time for the 1st Runner :")
runner1=float(input())
print("Enter the time for the 2nd Runner :")
runner2=float(input())
print("Enter the time for the 3rd Runner :")
runner3=float(input())
print("The average speed of the runner is")
avg_run=(runner1+runner2+runner3)/3
print(f'{avg_run} s')


