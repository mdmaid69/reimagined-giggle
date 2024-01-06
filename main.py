import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))