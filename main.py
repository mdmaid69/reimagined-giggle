import array
def convert_array_to_bytes(array):
        return array.tobytes()
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)