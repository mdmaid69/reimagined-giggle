  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])