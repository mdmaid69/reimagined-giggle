import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def count_words(sentence):
        return len(sentence.split())