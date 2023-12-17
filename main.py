import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)