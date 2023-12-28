def find_unique_words(sentence):
        return set(sentence.split())
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])