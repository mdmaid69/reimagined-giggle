import array
def insert_into_array(array, i, item):
        array.insert(i, item)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b