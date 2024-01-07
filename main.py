import array
def append_to_array(array, item):
        array.append(item)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)