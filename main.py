import os
def remove_directory(path):
        os.rmdir(path)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])