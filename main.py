import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import os
def list_files_in_directory(path):
        return os.listdir(path)