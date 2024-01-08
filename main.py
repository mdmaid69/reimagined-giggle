import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)