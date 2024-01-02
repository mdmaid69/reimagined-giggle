import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets