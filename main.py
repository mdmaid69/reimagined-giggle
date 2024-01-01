import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
i = 0
while i < 5:
        print(i)
        i += 1