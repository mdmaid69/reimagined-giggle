def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h