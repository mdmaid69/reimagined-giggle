  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
def is_palindrome(s):
        return s == s[::-1]