import array
def get_array_item(array, i):
        return array[i]
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)