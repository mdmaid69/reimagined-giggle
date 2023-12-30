import array
def get_array_as_float(array):
        return float(array[0])
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])