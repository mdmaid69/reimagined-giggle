import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
def is_even(n):
        return n % 2 == 0