import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)