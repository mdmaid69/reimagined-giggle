import os
def get_file_size(filename):
        return os.path.getsize(filename)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])