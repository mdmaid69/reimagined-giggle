import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())