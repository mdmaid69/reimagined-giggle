import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)