# some arithmetic operations of the list
# create a new list for fruits
fruits=[]
total=int(input("Enter the total number of items : "))
count=0
while count<total :
    f1=input('Enter the name of the fruits :')
# Added the items in the list
    fruits.append(f1)
    count=count+1
print(f"The list of the fruits is : \n {fruits}")

# create another list of students and take their total marks and sort the number of the list
marks=[]
number=int(input("Enter how many number of students marks do you want to enter : "))
count=0
while count<number :
    m=int(input("Enter the total marks of the student :"))
    marks.append(m)
    count=count+1
print(f"Enter list of the marks for the student: \n {marks}")
s=sorted(marks) # One way to sort the value of the list
marks.sort() # another way to sort the list
print(marks)
print(f"The list display as a sorted matter : \n {s}")
add=sum(marks)
print(f"The sum of the total number is : \n {add}")
# count the number of '0' in the following list
numeric=[12, 76, 0, 90, 0, 34]
l=len(numeric)
count=0
start=0
while start<l :
    if numeric[start] == 0 :
        count=count+1
    start=start+1
print(f"The count of total '0' in the given list: \n {count}")

