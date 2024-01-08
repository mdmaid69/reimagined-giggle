import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)