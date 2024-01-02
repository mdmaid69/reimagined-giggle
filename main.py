import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def find_unique_words(sentence):
        return set(sentence.split())