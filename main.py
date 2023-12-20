n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())