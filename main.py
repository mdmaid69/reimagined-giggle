  import os
  def get_directory_name(path):
        return os.path.dirname(path)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])