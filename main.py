import array
def get_array_as_list(array):
        return list(array)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)