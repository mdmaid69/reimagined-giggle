import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue