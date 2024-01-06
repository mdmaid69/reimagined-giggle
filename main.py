import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
n = 10
print("Square numbers:", [x**2 for x in range(n)])