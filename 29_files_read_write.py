# This is the code to check the different operations in file
#with open("user_info.txt", 'a') as file :
    #file.write("Manish : 847345776 \n" "Guru : 948824858 \n")
with open("user_info.txt", 'r') as file :
    user_read=file.readlines() # It will print as a list
    print("The content of the file is:")
    for info in user_read : # created a for loop to access the file
        print(info)
#with open("test.txt", 'a') as file:
    # write operation performed
    #file.write("This is additional content.\n I love to code in python. \n")
    # Read the content from the created file
#with open("test.txt", 'r') as file:
    # performed the read operation
    #content=file.read()
    #print(f"The content of the file 'test.txt' is: \n {content}")