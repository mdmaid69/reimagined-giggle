import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import time
print(time.time())