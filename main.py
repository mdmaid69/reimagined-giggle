import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import platform
def get_python_version():
        return platform.python_version()