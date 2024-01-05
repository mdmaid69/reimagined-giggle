import collections
def count_elements(iterable):
        return collections.Counter(iterable)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())