numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable