import array
def get_array_from_file(filename, typecode):
        a = array.array(typecode)
        with open(filename, "rb") as f:
        a.fromfile(f, os.path.getsize(filename) // a.itemsize)
        return a
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)