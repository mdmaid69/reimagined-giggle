import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))