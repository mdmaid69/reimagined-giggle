import collections
def create_ordered_dict():
        return collections.OrderedDict()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())