import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue