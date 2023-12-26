import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])