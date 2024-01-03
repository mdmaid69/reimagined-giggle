text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
def is_palindrome(s):
        return s == s[::-1]