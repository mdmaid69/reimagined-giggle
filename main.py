text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size