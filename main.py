import collections
def count_elements(iterable):
        return collections.Counter(iterable)
def find_unique_words(sentence):
        return set(sentence.split())