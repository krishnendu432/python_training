# How to use find() to search substring from a string
str1=input("Enter your statement :")
sub_str1=input("Enter the word which you want to check that is present in the statement or not :")
#str1="He is a leader of his village."
pos=str1.find(sub_str1)
if pos == -1 :
    print("Your searching word is not available in the existing statement.")
#    print(pos)
else :
    print("The position of the finding word in the statement is :")
    print(pos)
