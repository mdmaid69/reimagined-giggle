def is_palindrome(s):
        return s == s[::-1]
  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime