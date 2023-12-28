import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import os
def get_environment_variable(var):
        return os.getenv(var)