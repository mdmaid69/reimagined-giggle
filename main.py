  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])