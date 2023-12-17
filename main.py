import os
def get_environment_variable(var):
        return os.getenv(var)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)