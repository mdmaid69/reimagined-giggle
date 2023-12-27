def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable