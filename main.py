import array
def get_array_as_memoryview(array):
        return memoryview(array)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])