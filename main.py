import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def count_words(sentence):
        return len(sentence.split())