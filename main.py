import array
def get_array_index(array, item):
        return array.index(item)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)