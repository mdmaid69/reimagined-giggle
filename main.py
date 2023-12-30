import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()