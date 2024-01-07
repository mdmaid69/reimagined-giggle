import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])