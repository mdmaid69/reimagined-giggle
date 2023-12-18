import array
def pop_from_array(array, i=-1):
        return array.pop(i)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())