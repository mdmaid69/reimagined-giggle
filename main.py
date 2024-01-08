import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import os
def get_file_size(filename):
        return os.path.getsize(filename)