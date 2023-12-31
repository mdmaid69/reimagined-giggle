import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))