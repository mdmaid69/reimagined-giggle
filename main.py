  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))