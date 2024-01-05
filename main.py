import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)