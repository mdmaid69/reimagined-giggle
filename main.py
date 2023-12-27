import array
def append_to_array(array, item):
        array.append(item)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b