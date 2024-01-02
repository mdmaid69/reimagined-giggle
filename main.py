import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])