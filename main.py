  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)