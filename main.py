import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))