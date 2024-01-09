def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)