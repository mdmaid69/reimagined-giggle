import array
def check_if_array_contains_item(array, item):
        return item in array
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())