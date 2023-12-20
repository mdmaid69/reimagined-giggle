import array
def get_array_slice(array, i, j):
        return array[i:j]
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])