import array
def get_list_from_array(array):
        return array.tolist()
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)