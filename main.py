import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())