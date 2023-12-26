import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())