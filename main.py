import sys
def print_python_version():
        print(sys.version)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()