import array
def append_to_array(array, item):
        array.append(item)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())