import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def find_unique_words(sentence):
        return set(sentence.split())