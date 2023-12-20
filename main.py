text = "Hello, world!"
print("Characters:", len(text))
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())