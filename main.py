  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
def is_palindrome(s):
        return s == s[::-1]