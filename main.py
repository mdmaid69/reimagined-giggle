  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import collections
def create_counter():
        return collections.Counter()