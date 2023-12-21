import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps