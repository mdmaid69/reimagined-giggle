import array
def convert_array_to_list(array):
        return array.tolist()
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)