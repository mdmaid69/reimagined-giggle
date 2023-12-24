import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())