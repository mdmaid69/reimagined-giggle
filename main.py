def count_words(sentence):
        return len(sentence.split())
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])