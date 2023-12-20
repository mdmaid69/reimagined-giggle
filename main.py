import array
def get_array_as_bytearray(array):
        return bytearray(array)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())