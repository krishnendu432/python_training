import os

def print_directory_contents(directory):
    # List all files and directories in the given directory
    contents = os.listdir(directory) # Use the OS module to list the contents of the directory
    for item in contents:
        print(item)

# Example usage:
directory_path = '/Krishnendu'  # Replace with your directory path
print(f"Contents of directory '{directory_path}':")
print_directory_contents(directory_path)