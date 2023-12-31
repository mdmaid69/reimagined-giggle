import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)