import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
n = 10
print("Square numbers:", [x**2 for x in range(n)])