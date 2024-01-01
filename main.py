import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())