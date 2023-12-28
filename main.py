import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding