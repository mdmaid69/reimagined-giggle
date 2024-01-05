import array
def get_array_as_int(array):
        return int(array[0])
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())