  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
def is_palindrome(s):
        return s == s[::-1]