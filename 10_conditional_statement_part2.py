# This is script for elseif loop
#Perform numeric operation of given numbers
print("Enter the details of the students:")
print("Enter the marks for the Maths :")
# How to convert a by default string value to interger value
math=int(input())
eng=int(input("Enter the marks for the English :"))
science=int(input("Enter the marks for the Science :"))
com=int(input("Enter the marks for the Computer :"))
total=math+eng+science+com
if total >= 300:
    print("This is 1st devision with A+ grade.")
    print(f"Total marks of the student is: {total}")
elif total >=240:
    print("This is 1st devision with A grade.")
    print(f"Total marks of the student is: {total}")
elif total >=200 :
    print("This is 2nd devision.")
    print(f"Total marks of the student is: {total}")
else:
    print("This is 2nd devision.")
    print(f"Total marks of the student is: {total}")