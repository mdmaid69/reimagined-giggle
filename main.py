  def remove_duplicates(lst):
        return list(set(lst))
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)