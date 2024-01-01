import os
print(os.getcwd())
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])