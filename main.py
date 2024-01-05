import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
def find_unique_words(sentence):
        return set(sentence.split())