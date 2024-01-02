import getpass
def get_username():
        return getpass.getuser()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])