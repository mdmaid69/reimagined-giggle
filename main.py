import array
def get_array_item_count(array, item):
        return array.count(item)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())