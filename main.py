import array
def check_if_array_contains_item(array, item):
        return item in array
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b