import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import sys
def add_to_python_path(path):
        sys.path.append(path)