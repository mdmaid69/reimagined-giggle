import array
def get_array_index(array, item):
        return array.index(item)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)