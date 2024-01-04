import array
def get_array_buffer_info(array):
        return array.buffer_info()
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)