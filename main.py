import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
  import os
  def get_current_directory():
        return os.getcwd()