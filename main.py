text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import os
def remove_directory(path):
        os.rmdir(path)