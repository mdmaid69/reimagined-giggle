import array
def get_array_as_memoryview(array):
        return memoryview(array)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])