import collections
def create_user_string():
        return collections.UserString()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])