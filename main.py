import array
def convert_array_to_list(array):
        return array.tolist()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)