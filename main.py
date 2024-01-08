import array
def pop_from_array(array, i=-1):
        return array.pop(i)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)