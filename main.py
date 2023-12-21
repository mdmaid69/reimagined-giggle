  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
def is_palindrome(s):
        return s == s[::-1]