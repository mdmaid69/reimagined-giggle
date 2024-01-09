import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))