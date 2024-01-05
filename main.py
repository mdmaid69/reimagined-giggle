import array
def get_array_itemsize(array):
        return array.itemsize
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b