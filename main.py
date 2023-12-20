import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())