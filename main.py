import array
def get_array_buffer_info(array):
        return array.buffer_info()
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b