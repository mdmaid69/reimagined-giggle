import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def find_unique_words(sentence):
        return set(sentence.split())