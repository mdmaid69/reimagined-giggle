import array
def get_array_item(array, i):
        return array[i]
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())