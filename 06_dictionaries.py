# This script is used to perform the operation of dictionaries.
# Define a new dictionaries
score ={"Jaisawal" : 80, "GIll" : 74, "Sanju" :56, "Surya": 39}
print(" Scoreshett is: ")
print(score)
print("Want to check only keys of the dictionaries:")
print(score.keys())
# another way to get the complete value of the dictionaries along with keys we can use items function
print("scoresheet is different format")
print(score.items())
print("Check the type of class")
print(type(score))
# How to get the data from dictionaries. Here we no need to think about indexing.
print("Please find the score of the Sanju:")
print(score["Sanju"])
# If we want to avoid wrong typeing issue from dict, then we can use get()
# Suppose we want to know the value of Rahul, but Rahul is not available in the list
print("Please find the score of Rahul:")
print(score.get("Rahul"))
# How to added value in diecionaries in between
score["Hardik"]=55
print("After adding Hardik's score the new score sheet is")
print(score)
# How to remove value from dictionaries
print("After remove Surya's data from the list, the new score sheet is:")
del score["Surya"]
print(score)
#  Define the length of the dictionaries
print("Find the length of the dictonaries")
print(len(score))
# How to use pop function
print(score.pop("Hardik"))
print("After remove Hardik from the list, the new scoresheet is:")
print(score)

