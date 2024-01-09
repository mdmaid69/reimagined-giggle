import array
def get_array_as_int(array):
        return int(array[0])
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])