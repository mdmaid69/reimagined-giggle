import array
def get_list_from_array(array):
        return array.tolist()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)