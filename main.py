  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
def convert_to_octal(n):
        return oct(n)