import sys
def exit_program():
        sys.exit()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])