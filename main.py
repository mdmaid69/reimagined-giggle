def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
text = "Hello, world!"
print("Reversed:", text[::-1])