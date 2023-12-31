import array
def get_string_from_array(array):
        return array.tobytes()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)