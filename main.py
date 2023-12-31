text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())