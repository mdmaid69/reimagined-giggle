import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets