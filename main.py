text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
  import os
  def split_path(path):
        return os.path.split(path)