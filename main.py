  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
def is_palindrome(s):
        return s == s[::-1]