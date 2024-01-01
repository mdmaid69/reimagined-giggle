  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import os
def list_files_in_directory(path):
        return os.listdir(path)