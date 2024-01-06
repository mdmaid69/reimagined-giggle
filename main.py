import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps