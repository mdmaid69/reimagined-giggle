import array
def get_array_as_frozenset(array):
        return frozenset(array)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())