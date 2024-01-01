import array
def get_array_slice(array, i, j):
        return array[i:j]
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b