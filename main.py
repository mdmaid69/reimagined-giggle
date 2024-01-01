import datetime
print(datetime.datetime.now())
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()