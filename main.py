import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
def find_unique_words(sentence):
        return set(sentence.split())