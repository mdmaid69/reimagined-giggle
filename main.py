import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import platform
def get_os_info():
        return platform.uname()