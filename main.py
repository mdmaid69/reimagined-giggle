def is_palindrome(s):
        return s == s[::-1]
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])