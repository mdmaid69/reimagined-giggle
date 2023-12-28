  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
def is_palindrome(s):
        return s == s[::-1]