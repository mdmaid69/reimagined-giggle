import array
def get_array_as_bytes(array):
        return bytes(array)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])