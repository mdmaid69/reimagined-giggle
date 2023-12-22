import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)