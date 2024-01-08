n = 10
print("Powers of 2:", [2**x for x in range(n)])
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()