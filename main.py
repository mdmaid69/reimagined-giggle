  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
def is_palindrome(s):
        return s == s[::-1]