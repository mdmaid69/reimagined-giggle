import bisect
def binary_search(sorted_list, item):
        i = bisect.bisect_left(sorted_list, item)
        if i != len(sorted_list) and sorted_list[i] == item:
        return i
        else:
        return -1
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)