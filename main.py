n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable