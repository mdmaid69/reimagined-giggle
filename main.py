def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))