import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)