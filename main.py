import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())