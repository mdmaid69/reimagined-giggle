def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h