text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
def find_unique_words(sentence):
        return set(sentence.split())