import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b