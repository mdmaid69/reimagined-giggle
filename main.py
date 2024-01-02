n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable