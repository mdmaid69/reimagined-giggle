n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()