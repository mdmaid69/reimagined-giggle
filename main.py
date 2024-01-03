  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
def is_palindrome(s):
        return s == s[::-1]