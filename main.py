import array
def get_array_as_set(array):
        return set(array)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))