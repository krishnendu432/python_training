# Find the word from the string and replace with a word
str1=input("Enter your statement :")
sub_str1=input("Enter the word which you want to check that is present in the statement or not :")
#str1="He is a leader of his village."
pos=str1.find(sub_str1)
if pos == -1 :
    print("Your searching word is not available in the existing statement.")
#    print(pos)
else :
    print("Your searching word is available in the existing string. The position of your word is in the existing string:")
    print(pos)
    choice=input("Please press \"c\" to replace the word or else press \"q\" to exit from the script :")
    if choice.lower() == 'c' :
        rep=input("Enter the replace word : ")
        str2=str1.replace(sub_str1,rep)
        print(f"After replacement the word {rep}, the new string is: ")
        print(str2)
    elif choice.lower() == 'q':
        print("Thank you for using the script.")
    else:
        print("Your have entered a wrong option: ")


