import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))