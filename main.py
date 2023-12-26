import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
def find_unique_words(sentence):
        return set(sentence.split())