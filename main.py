  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)