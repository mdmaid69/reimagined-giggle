import platform
def get_python_version():
        return platform.python_version()
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()