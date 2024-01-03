import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())