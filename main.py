  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)