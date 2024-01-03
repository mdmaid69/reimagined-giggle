import array
def remove_from_array(array, item):
        array.remove(item)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)