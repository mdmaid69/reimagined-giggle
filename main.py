import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))