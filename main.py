for i in range(10): print(i)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()