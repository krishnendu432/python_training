# Write a program to take input from user as a marks.
# Individual subject '33' is the pass mark but for total average '40%' is required as a pass mark.
Lan=int(input("Enter the marks of the 1st Language Subject: "))
Eng=int(input("Enter the marks of the 1st English Subject: "))
Math=int(input("Enter the marks of the 1st Mathematics: "))
Science=int(input("Enter the marks of the 1st Science Subject: "))
Arts=int(input("Enter the marks of the 1st Arts Subject: "))
total_marks=Lan+Eng+Math+Science+Arts
avg=total_marks/5
if (avg>= 40) and (Lan >= 33) and (Eng >= 33) and (Math >= 33) and (Science>=33) and (Arts >=33)  :
    print(f" The student is passed. The percentage of the student is {avg} ")
    print(f"The marks of the student are\n Language : {Lan}, English : {Eng}, Math :{Math}, Science :{Science}, Arts: {Arts}")
else:
    print(f" The  student become failed. The average of the student is : {avg}")

# Write a program where we will take input as a post from user.
# We will check that the post is talking about predefine statement or not.
post = input("Enter you post : ")
check = input(" Enter the variable with which you want check your post ")
if (check.lower() in post.lower()) :
    print(f"The post is about {check}.")
else:
    print(f"The post is not about {check}.")