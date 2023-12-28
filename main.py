import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)