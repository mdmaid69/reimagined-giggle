def find_unique_words(sentence):
        return set(sentence.split())
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a