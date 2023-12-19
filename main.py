  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)