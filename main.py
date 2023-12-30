  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])