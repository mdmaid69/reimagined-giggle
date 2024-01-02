import array
def get_array_buffer_info(array):
        return array.buffer_info()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)