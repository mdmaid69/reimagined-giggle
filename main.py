  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import collections
def create_ordered_dict():
        return collections.OrderedDict()