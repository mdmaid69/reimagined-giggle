def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)