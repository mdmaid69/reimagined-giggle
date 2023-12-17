text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)