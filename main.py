import array
def get_array_as_memoryview(array):
        return memoryview(array)
n = 10
print("Square numbers:", [x**2 for x in range(n)])