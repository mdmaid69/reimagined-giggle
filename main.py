import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)