import array
def get_array_length(array):
        return len(array)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)