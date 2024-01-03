import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))