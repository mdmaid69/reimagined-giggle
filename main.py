  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
def is_palindrome(s):
        return s == s[::-1]