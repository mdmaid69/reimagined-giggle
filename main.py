import array
def get_bytes_from_array(array):
        return array.tobytes()
def find_unique_words(sentence):
        return set(sentence.split())