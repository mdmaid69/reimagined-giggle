import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)