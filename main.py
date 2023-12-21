import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)