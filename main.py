import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities