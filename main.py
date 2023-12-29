import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))