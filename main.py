import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def find_unique_words(sentence):
        return set(sentence.split())