import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)