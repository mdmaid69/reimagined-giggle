text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
  import os
  def get_base_name(path):
        return os.path.basename(path)