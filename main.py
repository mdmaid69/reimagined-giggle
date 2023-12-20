import array
def reverse_array(array):
        array.reverse()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())