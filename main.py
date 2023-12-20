import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)