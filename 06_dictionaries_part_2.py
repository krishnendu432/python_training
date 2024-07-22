# create a dictionary of students marks
student_marks={ "Amol" : 88,
    "Ranjit" : 92,
    "Partha" : 32
}
print("Display the dictionary of the student's marks:")
print(student_marks)
student=input("Enter name of the student for whom you want to check the marks: ")
print(student_marks[student])
# insert the students name and their marks from the user
student_marks={}
try :
    number=int(input("For how many students you want to insert their marks: "))
    count=0
    while count<number :
        name=input("Enter the name of the student: ")
        try:
            marks=int(input("Enter marks of the student: "))
            if marks < 0:
                print(f"Negative marks {marks} can't be entered.")
            else:
                student_marks.update({name:marks})
            count=count+1
        except Exception as e:
            print(e, type(e))
    print("Display the student name with their marks: ")
    print(student_marks)
except Exception as e:
    print(e,type(e))
