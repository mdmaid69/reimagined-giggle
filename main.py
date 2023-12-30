import os
print(os.getcwd())
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())