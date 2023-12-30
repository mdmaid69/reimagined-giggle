import array
def get_array_buffer_info(array):
        return array.buffer_info()
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])