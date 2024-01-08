  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
def reverse_string(s):
        return s[::-1]