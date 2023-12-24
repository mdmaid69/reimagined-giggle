import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b