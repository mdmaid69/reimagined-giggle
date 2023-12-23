import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)