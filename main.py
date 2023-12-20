import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])