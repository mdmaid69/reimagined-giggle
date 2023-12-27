import array
def append_to_array(array, item):
        array.append(item)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)