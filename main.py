import array
def set_array_item(array, i, item):
        array[i] = item
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())