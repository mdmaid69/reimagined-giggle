import array
def get_array_as_float(array):
        return float(array[0])
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)