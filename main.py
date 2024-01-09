import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())