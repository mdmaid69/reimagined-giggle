def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)