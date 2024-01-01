def calculate_payback_period(cash_flows):
        cumulative_cash_flow = 0
        for i, cf in enumerate(cash_flows):
        cumulative_cash_flow += cf
        if cumulative_cash_flow >= 0:
                return i
        return None
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)