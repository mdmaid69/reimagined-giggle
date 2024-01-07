text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import os
def change_working_directory(path):
        os.chdir(path)