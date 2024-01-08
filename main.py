import array
def remove_from_array(array, item):
        array.remove(item)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())