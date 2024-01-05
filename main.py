import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity