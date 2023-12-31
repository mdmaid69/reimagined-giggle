import array
def insert_into_array(array, i, item):
        array.insert(i, item)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)