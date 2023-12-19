def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)