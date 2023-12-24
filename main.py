import array
def insert_into_array(array, i, item):
        array.insert(i, item)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)