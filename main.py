import array
def get_array_as_memoryview(array):
        return memoryview(array)
n = 10
print("Powers of 2:", [2**x for x in range(n)])