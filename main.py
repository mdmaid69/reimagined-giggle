import array
def extend_array(array, iterable):
        array.extend(iterable)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))