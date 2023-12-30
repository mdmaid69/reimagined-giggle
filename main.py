def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
from collections import Counter
print(Counter("hello world"))