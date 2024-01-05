import os
def change_working_directory(path):
        os.chdir(path)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])