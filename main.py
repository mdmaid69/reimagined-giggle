import array
def get_array_buffer_info(array):
        return array.buffer_info()
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b