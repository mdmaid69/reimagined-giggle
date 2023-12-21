import collections
def create_stack():
        return collections.deque()
  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink