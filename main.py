  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import bisect
def binary_search(sorted_list, item):
        i = bisect.bisect_left(sorted_list, item)
        if i != len(sorted_list) and sorted_list[i] == item:
        return i
        else:
        return -1