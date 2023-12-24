import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])