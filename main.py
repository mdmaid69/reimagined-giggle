for i in range(5):
        print(i)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()