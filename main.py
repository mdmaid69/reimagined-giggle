def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)