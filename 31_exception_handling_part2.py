# this is the code to perform the exception handling
try : #It will check the file is available or not
    with open("user_info.txt", 'r') as file:
        content=file.readlines()
        print("The content of the file is:")
        for read in content:
            print(read)
#If the file is not available then catch the exception
except FileNotFoundError:
    print("The particular file is not available in the specific path")