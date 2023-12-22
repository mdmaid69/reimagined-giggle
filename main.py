import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def count_characters(sentence):
        return len(sentence)