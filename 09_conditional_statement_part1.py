# Write a program to take input from user as a marks.
# Individual subject '33' is the pass mark but for total average '40%' is required as a pass mark.
Lan=int(input("Enter the marks of the 1st Language Subject: "))
Eng=int(input("Enter the marks of the 1st English Subject: "))
#Math=int(input("Enter the marks of the 1st Mathematics: "))
#Science=int(input("Enter the marks of the 1st Science Subject: "))
#Arts=int(input("Enter the marks of the 1st Arts Subject: "))
total_marks=Lan+Eng
avg=total_marks/2
if (Lan > 33) and (Eng > 33) :
    print("Subject wise the student is passed. ")
    print(f"The marks of the student are\n Language : {Lan}, English : {Eng}")
elif avg > 40 :
    print(f"All total the student become passed {avg}")
else:
    print(f"all total the  student become failed {avg}")