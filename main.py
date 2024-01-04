import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])