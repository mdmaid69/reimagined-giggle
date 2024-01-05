import array
def get_array_as_bytes(array):
        return bytes(array)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())