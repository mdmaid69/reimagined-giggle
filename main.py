def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)