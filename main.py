  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)