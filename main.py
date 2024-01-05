import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def count_words(sentence):
        return len(sentence.split())