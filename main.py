import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import datetime
def get_current_datetime():
        return datetime.datetime.now()