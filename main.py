import array
def get_array_as_complex(array):
        return complex(array[0])
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())