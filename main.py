  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import collections
def create_user_list():
        return collections.UserList()