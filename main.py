import array
def get_array_as_float(array):
        return float(array[0])
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())