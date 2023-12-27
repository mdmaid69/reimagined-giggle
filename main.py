import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())