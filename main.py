import array
def get_array_as_memoryview(array):
        return memoryview(array)
def find_unique_words(sentence):
        return set(sentence.split())