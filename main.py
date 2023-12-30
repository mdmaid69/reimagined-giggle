import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)