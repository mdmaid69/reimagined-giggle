import array
def get_array_as_list(array):
        return list(array)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())