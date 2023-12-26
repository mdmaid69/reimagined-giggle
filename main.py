import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))