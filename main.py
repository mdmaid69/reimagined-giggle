def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h