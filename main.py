import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def find_unique_words(sentence):
        return set(sentence.split())