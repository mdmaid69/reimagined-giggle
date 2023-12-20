import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import time
def get_current_time():
        return time.ctime()