import array
def pop_from_array(array, i=-1):
        return array.pop(i)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b