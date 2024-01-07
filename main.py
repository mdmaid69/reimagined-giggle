def find_unique_words(sentence):
        return set(sentence.split())
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a