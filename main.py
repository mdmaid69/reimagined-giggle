  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
def is_palindrome(s):
        return s == s[::-1]