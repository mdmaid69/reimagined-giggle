import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])