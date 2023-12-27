sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])