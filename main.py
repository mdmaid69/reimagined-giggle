def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h