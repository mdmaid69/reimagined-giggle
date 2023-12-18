import array
def get_array_slice(array, i, j):
        return array[i:j]
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())