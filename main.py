text = "Hello, world!"
print("Words:", len(text.split()))
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())