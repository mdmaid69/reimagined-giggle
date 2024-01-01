text = "Hello, world!"
print("Uppercase:", text.upper())
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())