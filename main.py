import collections
def create_ordered_dict():
        return collections.OrderedDict()
  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime