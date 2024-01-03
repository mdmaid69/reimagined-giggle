  def remove_duplicates(lst):
        return list(set(lst))
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)