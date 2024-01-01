def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)