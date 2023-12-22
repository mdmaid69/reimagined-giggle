import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)