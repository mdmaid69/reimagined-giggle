def count_words(sentence):
        return len(sentence.split())
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))