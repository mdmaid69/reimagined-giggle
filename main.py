def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)