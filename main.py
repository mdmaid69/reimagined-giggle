import array
def append_to_array(array, item):
        array.append(item)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)