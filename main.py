  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])