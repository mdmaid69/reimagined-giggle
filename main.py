import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
print([x**2 for x in range(10)])