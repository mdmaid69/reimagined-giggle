  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])