n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable