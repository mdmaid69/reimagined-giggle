  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
def is_palindrome(s):
        return s == s[::-1]