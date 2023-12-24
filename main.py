import os
def list_files_in_directory(path):
        return os.listdir(path)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])