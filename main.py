def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array