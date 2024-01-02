import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])