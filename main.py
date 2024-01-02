  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
def is_palindrome(s):
        return s == s[::-1]