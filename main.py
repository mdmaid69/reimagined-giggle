def is_palindrome(s):
        return s == s[::-1]
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))