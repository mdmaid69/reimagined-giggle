import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
n = 10
print("Cube numbers:", [x**3 for x in range(n)])