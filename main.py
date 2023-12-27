import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())