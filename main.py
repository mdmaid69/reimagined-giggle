import shutil
def delete_directory(path):
        shutil.rmtree(path)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)