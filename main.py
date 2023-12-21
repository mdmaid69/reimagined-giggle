import array
def get_array_as_bytearray(array):
        return bytearray(array)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))