  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)