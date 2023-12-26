import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))