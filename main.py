import sys
def add_to_python_path(path):
        sys.path.append(path)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])