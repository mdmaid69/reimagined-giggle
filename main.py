n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)