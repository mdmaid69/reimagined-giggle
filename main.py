def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)