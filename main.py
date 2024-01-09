import array
def extend_array(array, iterable):
        array.extend(iterable)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())