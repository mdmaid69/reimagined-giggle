import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
def count_words(sentence):
        return len(sentence.split())