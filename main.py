import array
def extend_array(array, iterable):
        array.extend(iterable)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])