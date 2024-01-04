import array
def get_array_as_frozenset(array):
        return frozenset(array)
def find_unique_words(sentence):
        return set(sentence.split())