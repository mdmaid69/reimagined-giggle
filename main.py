import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))