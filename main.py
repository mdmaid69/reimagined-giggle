import array
def get_string_from_array(array):
        return array.tobytes()
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)