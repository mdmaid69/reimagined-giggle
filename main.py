import array
def get_array_as_frozenset(array):
        return frozenset(array)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))