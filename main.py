import array
def pop_from_array(array, i=-1):
        return array.pop(i)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)