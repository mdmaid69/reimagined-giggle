import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
i = 0
while i < 5:
        print(i)
        i += 1