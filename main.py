import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
print(sum(range(10)))