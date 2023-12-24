import array
def insert_into_array(array, i, item):
        array.insert(i, item)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)