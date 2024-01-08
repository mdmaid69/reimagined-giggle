import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
def count_words(sentence):
        return len(sentence.split())