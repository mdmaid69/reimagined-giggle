def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)