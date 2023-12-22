import re
print(re.match("h.*o", "hello world"))
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])