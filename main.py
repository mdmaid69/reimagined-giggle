import array
def get_array_as_memoryview(array):
        return memoryview(array)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))