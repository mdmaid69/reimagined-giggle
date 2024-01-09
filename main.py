import array
def insert_into_array(array, i, item):
        array.insert(i, item)
def find_unique_words(sentence):
        return set(sentence.split())