def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)