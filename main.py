text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)