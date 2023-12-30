import array
def clear_array(array):
        array *= 0
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())