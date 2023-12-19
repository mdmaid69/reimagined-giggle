import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)