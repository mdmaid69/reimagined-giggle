import bisect
def binary_search(sorted_list, item):
        i = bisect.bisect_left(sorted_list, item)
        if i != len(sorted_list) and sorted_list[i] == item:
        return i
        else:
        return -1
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)