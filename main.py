  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
def is_palindrome(s):
        return s == s[::-1]