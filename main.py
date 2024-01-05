import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities