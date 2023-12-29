import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
def find_unique_words(sentence):
        return set(sentence.split())