# This script is used to perform the operation of dictionaries.
# Define a new dictionaries
score ={"Jaisawal" : 80, "GIll" : 74, "Sanju" :56, "Surya": 39}
print(" Score sheet is: ")
print(score)
print("Want to check only keys of the dictionaries:")
print(score.keys())
print("Want to check only values of the dictionaries:")
print(score.values())
# another way to get the complete value of the dictionaries along with keys we can use items function
print("score sheet is different format")
print(score.items())
print("Check the type of class")
print(type(score))
# How to get the data from dictionaries. Here we, no need to think about indexing.
print("Please find the score of the Sanju:")
print(score["Sanju"])
# If we want to avoid wrong typing issue from dict, then we can use get()
# Suppose we want to know the value of Rahul, but Rahul is not available in the list
print("Please find the score of Rahul:")
print(score.get("Rahul"))
# How to add value in dictionaries in between
score["Hardik"]=55
print("After adding Hardik's score the new score sheet is")
print(score)
# Update the score of the Sanju
print("Update the score of the Sanju: \n")
score.update({"Sanju":110})
print(score["Sanju"])
print(f"After update the score of Sanju the score sheet is :- \n {score}")
# How to remove value from dictionaries
print("After remove Surya's data from the list, the new score sheet is:")
del score["Surya"]
print(score)
#  Define the length of the dictionaries
print("Find the length of the dictionaries")
print(len(score))
# How to use pop function
print(score.pop("Hardik"))
print("After remove Hardik from the list, the new scoresheet is:")
print(score)

