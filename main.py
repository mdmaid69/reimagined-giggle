import time
def get_time_since_epoch():
        return time.time()
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()