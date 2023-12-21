import array
def get_array_as_memoryview(array):
        return memoryview(array)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())