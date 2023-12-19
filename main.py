import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
def count_words(sentence):
        return len(sentence.split())