import array
def get_array_as_int(array):
        return int(array[0])
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b