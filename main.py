import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets