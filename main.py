import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))