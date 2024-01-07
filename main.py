import collections
def create_ordered_dict():
        return collections.OrderedDict()
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]