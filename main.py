  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
def is_palindrome(s):
        return s == s[::-1]