text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)