import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)