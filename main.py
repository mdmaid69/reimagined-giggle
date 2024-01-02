def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import os
print(os.getcwd())