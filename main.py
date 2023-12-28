  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import bisect
def binary_search(sorted_list, item):
        i = bisect.bisect_left(sorted_list, item)
        if i != len(sorted_list) and sorted_list[i] == item:
        return i
        else:
        return -1