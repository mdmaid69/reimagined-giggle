  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))