n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import platform
def get_os_info():
        return platform.uname()