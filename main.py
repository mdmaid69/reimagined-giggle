import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def count_words(sentence):
        return len(sentence.split())