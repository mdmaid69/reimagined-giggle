import collections
def create_counter():
        return collections.Counter()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())