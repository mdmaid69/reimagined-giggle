import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def count_characters(sentence):
        return len(sentence)