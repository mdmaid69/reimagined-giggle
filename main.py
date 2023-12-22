def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)