  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import os
def get_file_size(filename):
        return os.path.getsize(filename)