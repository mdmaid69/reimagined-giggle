import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))