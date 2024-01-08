import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()