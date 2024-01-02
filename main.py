import array
def get_array_as_str(array):
        return str(array)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())