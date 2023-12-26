import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)