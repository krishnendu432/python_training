class MySchool:
  SCHOOL="The Student High School"
  def __init__(self, name, ID, age, email):  # Constructor
    self.name = name
    self.ID = ID
    self.age = age
    self.email = email

  def student_info(self):
    """Prints the student information in a formatted way."""
    print("Please verify the student details:")
    print(f"Student Name: {self.name}")
    print(f"Student ID: {self.ID}")
    print(f"Student Age: {self.age}")
    print(f"Student Email: {self.email}")

  def change_info(self, new_age, new_email):
    """Updates the student's age and email address."""
    self.age = new_age  # Update the age attribute
    self.email = new_email  # Update the email attribute
    print("Student information updated successfully!")

    # You can now call student_info() to see the updated information

# Get user input for student information
print("Provide the below required details:")
name = input("Enter the name of the student: ")
ID = input("Enter the ID of the student: ")
age = int(input("Enter the age of the student: "))
email = input("Enter the email ID of the student: ")

# Create the object using the user input
student = MySchool(name, ID, age, email)
print("Name of the school is :")
print(student.SCHOOL)

# Call the student_info method to display information
student.student_info()
active=True
while active :
  choice=input("If you want to modify the student details press 'y' or press 'q' to quit from the script")
  if choice.lower()=='y' :
# Get user input for modification
    new_age = int(input("Enter the new age of the student : "))
    new_email = input("Enter the new email ID of the student: ")
# Call the change_info method to update information
    student.change_info(new_age, new_email)
  elif choice.lower() =='q' :
    active=False
  else:
    print("It's an invalid choice. Please press 'y' or 'q' for further process: ")
# Call student_info again to see the updated details (optional)
student.student_info()

