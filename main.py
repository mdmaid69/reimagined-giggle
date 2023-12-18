import array
def pop_from_array(array, i=-1):
        return array.pop(i)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)