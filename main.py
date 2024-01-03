print(sum(range(10)))
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()