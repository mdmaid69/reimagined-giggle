import os
def remove_directory(path):
        os.rmdir(path)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()