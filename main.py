  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])