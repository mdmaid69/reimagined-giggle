import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue