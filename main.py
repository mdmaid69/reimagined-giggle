import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)