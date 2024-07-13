# Write a script to remove the duplicate digit from the list

num=[24, 28, 32, 28, 45, 28]
print("The value of the list is :")
print(num)
while 28 in num :
#The below function helped us to remove the duplicate digit from the list
    num.remove(28)
print("Display the list after removed the duplicate digit from the list")
print(num)