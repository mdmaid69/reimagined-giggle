import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)