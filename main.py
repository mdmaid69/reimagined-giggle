import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue