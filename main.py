import array
def get_array_buffer_info(array):
        return array.buffer_info()
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])