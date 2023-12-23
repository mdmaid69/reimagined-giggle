import array
def clear_array(array):
        array *= 0
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)