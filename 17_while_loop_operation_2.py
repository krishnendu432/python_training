# This is another way to use while loop
# import math library
import math
active=True
#Thw 'while' loop will work till the active value is become False
while active :
    num= input(" Please enter the number to check the square root of the digit or else press 'q' to exit:")
    if num.isdigit() :
        digit=math.sqrt(int(num))
        print(f" The square root of the number {num} is : {digit}")
    if num.lower() =='q':
        active=False
print("Now you exit from the script :")
