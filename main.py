import getpass
def get_username():
        return getpass.getuser()
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()