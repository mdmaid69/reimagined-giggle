print([x**2 for x in range(10)])
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()