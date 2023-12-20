import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())