import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())