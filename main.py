import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)