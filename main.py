def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))