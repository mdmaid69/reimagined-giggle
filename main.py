def find_unique_words(sentence):
        return set(sentence.split())
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))