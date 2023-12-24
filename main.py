n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a