import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)