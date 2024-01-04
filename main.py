import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])