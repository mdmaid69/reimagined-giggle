import collections
def create_user_dict():
        return collections.UserDict()
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]