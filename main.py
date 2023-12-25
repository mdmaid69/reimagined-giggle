n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()