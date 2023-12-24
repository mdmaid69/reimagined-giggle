import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities