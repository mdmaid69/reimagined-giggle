import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
n = 10
print("Powers of 2:", [2**x for x in range(n)])