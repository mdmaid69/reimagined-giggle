import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b