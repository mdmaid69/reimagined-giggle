import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def count_words(sentence):
        return len(sentence.split())