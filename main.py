import collections
def count_elements(iterable):
        return collections.Counter(iterable)
def count_words(sentence):
        return len(sentence.split())