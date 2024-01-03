import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)