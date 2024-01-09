import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))