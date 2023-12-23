def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)