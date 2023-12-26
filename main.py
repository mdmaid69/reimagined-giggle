def count_characters(sentence):
        return len(sentence)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)