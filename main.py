  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import bisect
def binary_search(sorted_list, item):
        i = bisect.bisect_left(sorted_list, item)
        if i != len(sorted_list) and sorted_list[i] == item:
        return i
        else:
        return -1