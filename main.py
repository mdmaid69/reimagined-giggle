import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
n = 10
print("Cube numbers:", [x**3 for x in range(n)])