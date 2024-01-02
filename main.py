import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)