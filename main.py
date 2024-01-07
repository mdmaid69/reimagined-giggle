def count_characters(sentence):
        return len(sentence)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])