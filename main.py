import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
def count_words(sentence):
        return len(sentence.split())