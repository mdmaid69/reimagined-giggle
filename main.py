import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)