n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)