  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import collections
def create_ordered_dict():
        return collections.OrderedDict()