import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()