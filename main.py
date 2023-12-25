def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)