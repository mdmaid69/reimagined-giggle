import re
def split_string(pattern, string):
        return re.split(pattern, string)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()