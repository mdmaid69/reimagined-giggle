import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])