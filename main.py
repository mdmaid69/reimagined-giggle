import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)