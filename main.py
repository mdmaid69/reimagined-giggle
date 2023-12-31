import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
n = 10
print("Square numbers:", [x**2 for x in range(n)])