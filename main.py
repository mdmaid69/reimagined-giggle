  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])