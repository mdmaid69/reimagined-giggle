import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)