import array
def set_array_item(array, i, item):
        array[i] = item
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])