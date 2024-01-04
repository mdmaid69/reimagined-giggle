import array
def set_array_item(array, i, item):
        array[i] = item
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b