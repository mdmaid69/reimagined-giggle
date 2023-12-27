import sys
def exit_program():
        sys.exit()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)