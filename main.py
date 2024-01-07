n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)