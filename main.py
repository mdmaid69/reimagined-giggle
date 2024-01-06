  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import os
def remove_directory(path):
        os.rmdir(path)