import platform
def get_python_version():
        return platform.python_version()
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)