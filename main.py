import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
i = 0
while i < 5:
        print(i)
        i += 1