import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])