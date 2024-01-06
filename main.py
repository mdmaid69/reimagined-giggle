import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()