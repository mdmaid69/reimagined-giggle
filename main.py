import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import sys
def exit_program():
        sys.exit()