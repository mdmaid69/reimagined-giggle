import collections
def count_elements(iterable):
        return collections.Counter(iterable)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)