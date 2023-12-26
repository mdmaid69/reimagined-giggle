import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())