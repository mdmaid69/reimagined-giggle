  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
def is_palindrome(s):
        return s == s[::-1]