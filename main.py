  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
def is_palindrome(s):
        return s == s[::-1]