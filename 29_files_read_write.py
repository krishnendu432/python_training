# This is the code to check the different operations in file
#with open("D:\Krishnendu\user_info.txt", 'w') as file :
    #file.write("This is test file using python")

#with open("user_info.txt", 'a') as file:
    # write operation performed
    #file.write("This is additional content.\n I love to code in python. \n")
    # Read the content from the created file
with open("user_info.txt", 'r') as file:
    # performed the read operation
    content=file.read()
    print(f"The content of the file is: \n {content}")