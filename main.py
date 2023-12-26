import sys
def exit_program():
        sys.exit()
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)