import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)