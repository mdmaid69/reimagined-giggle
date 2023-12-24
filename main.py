import array
def set_array_item(array, i, item):
        array[i] = item
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)