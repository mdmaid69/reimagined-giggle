text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
def count_words(sentence):
        return len(sentence.split())