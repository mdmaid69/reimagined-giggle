import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities