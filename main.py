import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
text = "Hello, world!"
print("Uppercase:", text.upper())