import array
def get_array_as_memoryview(array):
        return memoryview(array)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])