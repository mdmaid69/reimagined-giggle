def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)