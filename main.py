import array
def get_array_as_repr(array):
        return repr(array)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())