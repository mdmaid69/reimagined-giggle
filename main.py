  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])