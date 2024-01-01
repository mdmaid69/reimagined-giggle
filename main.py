import array
def convert_array_to_list(array):
        return array.tolist()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())