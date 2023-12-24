import sys
print(sys.version)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()