  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import bisect
def binary_search(sorted_list, item):
        i = bisect.bisect_left(sorted_list, item)
        if i != len(sorted_list) and sorted_list[i] == item:
        return i
        else:
        return -1