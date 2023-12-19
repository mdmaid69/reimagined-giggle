import array
def convert_array_to_bytes(array):
        return array.tobytes()
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)