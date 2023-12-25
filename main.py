import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue