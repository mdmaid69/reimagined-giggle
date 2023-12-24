  import os
  def delete_file(file_name):
        os.remove(file_name)
def is_palindrome(s):
        return s == s[::-1]