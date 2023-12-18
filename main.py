import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])