import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import os
def get_environment_variable(var):
        return os.getenv(var)