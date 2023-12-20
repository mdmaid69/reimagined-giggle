import sys
print(sys.version)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())