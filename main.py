import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))