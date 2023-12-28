import os
def change_working_directory(path):
        os.chdir(path)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()